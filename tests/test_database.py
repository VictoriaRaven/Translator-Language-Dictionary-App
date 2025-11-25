import os
import sqlite3
import tempfile
import importlib

import pytest

import settings
import database


# ----------------------------
# Use a temp database per test
# ----------------------------
def use_temp_db(monkeypatch):
    """Create an isolated temporary DB and patch settings.DB_NAME."""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
    db_path = tmp.name
    tmp.close()                       # Required for Windows

    monkeypatch.setattr(settings, "DB_NAME", db_path)

    # Reinitialize module-level code (init_db reads DB_NAME)
    importlib.reload(database)
    database.init_db()

    return db_path


# ----------------------------------
#        TESTS BEGIN HERE
# ----------------------------------

def test_init_db_creates_tables(monkeypatch):
    db_path = use_temp_db(monkeypatch)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {row[0] for row in cur.fetchall()}
    conn.close()

    assert "dictionary" in tables
    assert "history" in tables


def test_insert_dictionary_row(monkeypatch):
    db_path = use_temp_db(monkeypatch)

    database.insert_dictionary_row("Hello", "Hola", "es")

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT word, translation, language FROM dictionary")
    row = cur.fetchone()

    conn.close()

    assert row is not None
    assert row[0] == "hello"        # lowercase enforced
    assert row[1] == "hola"
    assert row[2] == "es"


def test_update_dictionary_row(monkeypatch):
    db_path = use_temp_db(monkeypatch)

    database.insert_dictionary_row("hi", "salut", "fr")

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id FROM dictionary")
    row_id = cur.fetchone()[0]
    conn.close()

    database.update_dictionary_row(row_id, "hello", "bonjour", "fr")

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT word, translation FROM dictionary WHERE id=?", (row_id,))
    row = cur.fetchone()
    conn.close()

    assert row[0] == "hello"
    assert row[1] == "bonjour"


def test_delete_dictionary_row(monkeypatch):
    db_path = use_temp_db(monkeypatch)

    database.insert_dictionary_row("cat", "gato", "es")

    # get id
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id FROM dictionary")
    row_id = cur.fetchone()[0]
    conn.close()

    database.delete_dictionary_row(row_id)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM dictionary")
    count = cur.fetchone()[0]
    conn.close()

    assert count == 0


def test_query_dictionary(monkeypatch):
    db_path = use_temp_db(monkeypatch)

    database.insert_dictionary_row("cat", "gato", "es")
    database.insert_dictionary_row("dog", "perro", "es")

    rows, total = database.query_dictionary(filter_text="ca")

    assert total == 1
    assert rows[0][1] == "cat"


def test_save_history_and_query_history(monkeypatch):
    db_path = use_temp_db(monkeypatch)

    database.save_history("hello", "hola", "es", used_online=True)

    rows, total = database.query_history()

    assert total == 1
    r = rows[0]
    assert r[1] == "hello"
    assert r[2] == "hola"
    assert r[3] == "es"
    assert r[4] == 1  # used_online=True stored as 1
