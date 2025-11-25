import pytest
from unittest.mock import patch
from yourmodule.translation import sql_translate, online_translate
from yourmodule.database import init_db, insert_dictionary_row
import tempfile

def test_sql_translate_found():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    init_db(tmp.name)
    insert_dictionary_row(tmp.name, "cat", "gato", "en", "es")

    result = sql_translate(tmp.name, "cat")
    assert result == "gato"

def test_sql_translate_not_found():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    init_db(tmp.name)
    assert sql_translate(tmp.name, "missing") is None

@patch("yourmodule.translation.GoogleTranslator.translate")
def test_online_translate_success(mock_trans):
    mock_trans.return_value = "gato"
    assert online_translate("cat", "en", "es") == "gato"

@patch("yourmodule.translation.GoogleTranslator.translate", side_effect=Exception("API error"))
def test_online_translate_failure(mock_trans):
    with pytest.raises(Exception):
        online_translate("cat", "en", "es")