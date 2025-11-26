from settings import DB_NAME
import os
import tempfile
import pytest
from unittest.mock import patch, MagicMock
import gui
from typing import cast, Callable
# ---------------------------
# TEST settings.py VALUES
# ---------------------------
if os.environ.get("TEST_MODE") == "1":
    import tkinter
    tkinter.Tk = lambda: None  # prevent real window

def test_lang_options_structure():
    from settings import LANG_OPTIONS

    assert isinstance(LANG_OPTIONS, list)
    for name, code in LANG_OPTIONS:
        assert isinstance(name, str)
        assert isinstance(code, str)
        assert len(code) >= 2


def test_txt_files_exist_or_are_valid_paths():
    from settings import TXT_FILES

    assert isinstance(TXT_FILES, dict)
    for code, path in TXT_FILES.items():
        assert isinstance(code, str)
        assert isinstance(path, str)
        assert "data/" in path


def test_deep_translator_flag():
    from settings import DEEP_TRANSLATOR_AVAILABLE
    assert isinstance(DEEP_TRANSLATOR_AVAILABLE, bool)


def test_db_name_is_inside_data_folder():
    assert os.path.basename(DB_NAME) == "translations.db"
    assert "data" in DB_NAME.replace("\\", "/").split("/")


# --------------------------------------------------------
# SYSTEM TEST: TranslatorApp → SQL + Save Integration
# --------------------------------------------------------

@patch("gui.save_history")
@patch("gui.sql_translate")
def test_system_translate_and_save(mock_sql, mock_save, monkeypatch):
    mock_sql.return_value = ("hola", False)

    # Avoid Tk mainloop
    monkeypatch.setattr(gui.tk.Tk, "mainloop", lambda self: None)

    app = gui.TranslatorApp(test_mode=True)

    # Correct mock for tk.Text.get
    app.word_input.get = cast(Callable[..., str], lambda index1="0.0", index2="end": "hello")
    app.lang_var.set(gui.LANG_OPTIONS[0][0])

    app.translate()

    mock_sql.assert_called_once()
    mock_save.assert_called_once_with(
        "hello", "hola", gui.LANG_OPTIONS[0][0], used_online=False
    )


# --------------------------------------------------------
# TEST: Online Translation Toggle
# --------------------------------------------------------

# tests/test_system.py
def test_online_translation_toggle():
    app = gui.TranslatorApp(test_mode=True)
    app.use_online_var.set(1)
    assert app.use_online_var.get() == 1

    app.use_online_var.set(0)
    assert app.use_online_var.get() == 0



# --------------------------------------------------------
# TEST: Online Translation Call
# --------------------------------------------------------

@patch("gui.online_translate")
def test_online_translation_call(mock_online, app):
    mock_online.return_value = "hola"
    app.use_online_var.set(1)

    app.word_input.get = lambda *a: "hello"
    app.lang_var.set("Spanish")

    app.translate()

    mock_online.assert_called_once()

