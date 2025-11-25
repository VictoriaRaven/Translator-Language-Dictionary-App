import pytest
from unittest.mock import patch, MagicMock
from yourmodule.gui.dictionary import DictionaryWindow

@pytest.fixture
def mock_root():
    return MagicMock()

@pytest.fixture
def gui(mock_root):
    return DictionaryWindow(mock_root, db_path=":memory:")

@patch("yourmodule.gui.dictionary.messagebox.showinfo")
@patch("yourmodule.gui.dictionary.messagebox.showerror")
@patch("yourmodule.gui.dictionary.sql_translate")
def test_translate_button_sql(mock_sql, mock_error, mock_info, gui):
    mock_sql.return_value = "hola"
    gui.word_entry.get = lambda: "hello"

    gui.translate_word()

    mock_info.assert_called()
    assert mock_sql.called

@patch("yourmodule.gui.dictionary.online_translate")
@patch("yourmodule.gui.dictionary.messagebox.showinfo")
@patch("yourmodule.gui.dictionary.messagebox.showerror")
def test_translate_button_online(mock_info, mock_error, mock_online, gui):
    mock_online.return_value = "bonjour"
    gui.word_entry.get = lambda: "hello"
    gui.lang_from.get = lambda: "en"
    gui.lang_to.get = lambda: "fr"

    gui.translate_online()

    mock_info.assert_called()

@patch("yourmodule.gui.dictionary.insert_dictionary_row")
@patch("yourmodule.gui.dictionary.messagebox.showinfo")
@patch("yourmodule.gui.dictionary.messagebox.showerror")
def test_add_word(mock_error, mock_info, mock_insert, gui):
    gui.word_entry.get = lambda: "cat"
    gui.result_label.config = lambda text: None

    gui.translation_text = "gato"
    gui.add_to_database()

    mock_insert.assert_called()
    mock_info.assert_called()