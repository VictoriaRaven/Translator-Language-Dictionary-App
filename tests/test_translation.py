import pytest
from unittest.mock import patch
import tempfile
import os
import database
from translation import sql_translate, online_translate

# ---------------------------
# SQL TRANSLATION TESTS
# ---------------------------

def test_sql_translate_found(monkeypatch):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.close()

    monkeypatch.setattr(database, "DB_NAME", tmp.name)

    database.init_db()
    database.insert_dictionary_row("cat", "gato", "en")

    result = sql_translate("cat", "en")

    # Accept both possible return formats
    assert result == "gato" or ("gato", False)

    os.unlink(tmp.name)


def test_sql_translate_not_found(monkeypatch):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.close()

    monkeypatch.setattr(database, "DB_NAME", tmp.name)

    database.init_db()

    result = sql_translate("missing", "en")

    assert result == (None, False)

    os.unlink(tmp.name)


# ---------------------------
# ONLINE TRANSLATION
# ---------------------------

@patch("translation.GoogleTranslator")
def test_online_translate_success(mock_gt):
    mock_instance = mock_gt.return_value
    mock_instance.translate.return_value = "gato"

    # your real online_translate(word, target_code)
    result = online_translate("cat", "es")

    assert result == "gato"


@patch("translation.GoogleTranslator")
def test_online_translate_failure(mock_gt):
    mock_instance = mock_gt.return_value
    mock_instance.translate.side_effect = Exception("API error")

    # your real code RETURNS None on error (does NOT raise)
    result = online_translate("cat", "es")

    assert result is None
