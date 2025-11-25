from unittest.mock import patch, MagicMock
import tempfile

@patch("yourmodule.gui.dictionary.sql_translate", return_value="hola")
@patch("yourmodule.gui.dictionary.insert_dictionary_row")
def test_system_translate_and_save(mock_insert, mock_sql):
    from yourmodule.gui.dictionary import DictionaryWindow

    fake_root = MagicMock()
    gui = DictionaryWindow(fake_root, db_path=":memory:")

    gui.word_entry.get = lambda: "hello"
    gui.translate_word()

    gui.translation_text = "hola"
    gui.add_to_database()

    mock_insert.assert_called()
    mock_sql.assert_called()