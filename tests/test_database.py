import sqlite3
import tempfile
from yourmodule.database import (
    init_db,
    insert_dictionary_row,
    update_dictionary_row,
    delete_dictionary_row,
    query_dictionary,
    save_history,
    query_history,
)

def create_temp_db():
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
    init_db(tmp.name)
    return tmp.name

def test_init_db_creates_tables():
    path = create_temp_db()
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {row[0] for row in cur.fetchall()}
    assert "dictionary" in tables
    assert "history" in tables

def test_insert_and_query_dictionary():
    path = create_temp_db()
    insert_dictionary_row(path, "Hello", "Hola", "en", "es")

    rows, total = query_dictionary(path, search="hello")
    assert total == 1
    assert rows[0][1] == "hello"
    assert rows[0][2] == "hola"

def test_update_dictionary_row():
    path = create_temp_db()
    insert_dictionary_row(path, "Hello", "Hola", "en", "es")

    rows, _ = query_dictionary(path, search="hello")
    row_id = rows[0][0]

    update_dictionary_row(path, row_id, "Hi", "Ola", "en", "pt")

    rows2, _ = query_dictionary(path, search="hi")
    assert rows2[0][1] == "hi"
    assert rows2[0][2] == "ola"

def test_delete_dictionary_row():
    path = create_temp_db()
    insert_dictionary_row(path, "Hello", "Hola", "en", "es")

    rows, _ = query_dictionary(path, search="hello")
    row_id = rows[0][0]

    delete_dictionary_row(path, row_id)

    rows2, total2 = query_dictionary(path, search="hello")
    assert total2 == 0

def test_save_and_query_history():
    path = create_temp_db()
    save_history(path, "hello", "hola", used_online=True)

    rows, total = query_history(path, search="hello")
    assert total == 1
    assert rows[0][1] == "hello"
    assert rows[0][2] == "hola"
    assert rows[0][3] == 1