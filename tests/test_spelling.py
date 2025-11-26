import pytest
from typing import Callable

from spelling import (
    auto_correct,
    SPELL_CHECKER,
    LANGUAGE_TOOL_AVAILABLE,
    SYM_AVAILABLE,
    UKRAINIAN_CHARS,
)
import spelling


# ------------------------------------------------------------
# BASIC TESTS
# ------------------------------------------------------------
def test_autocorrect_returns_string():
    result = auto_correct("hello")
    assert isinstance(result, str)

def test_autocorrect_empty_string():
    assert auto_correct("") == ""

def test_autocorrect_no_crash():
    assert isinstance(auto_correct("heelo"), str)
# ------------------------------------------------------------
# LANGUAGE TOOL TESTS
# ------------------------------------------------------------
@pytest.mark.skipif(not LANGUAGE_TOOL_AVAILABLE, reason="LanguageTool not installed")
def test_languagetool_correction_english(monkeypatch):
    monkeypatch.setattr("spelling.auto_correct", lambda w: "hello")
    result = spelling.auto_correct("heelo")
    assert result == "hello"

@pytest.mark.skipif(not LANGUAGE_TOOL_AVAILABLE, reason="LanguageTool not installed")
def test_languagetool_no_change_for_correct_word(monkeypatch):
    monkeypatch.setattr("spelling.auto_correct", lambda w: "hello")
    result = spelling.auto_correct("hello")
    assert result == "hello"
# ------------------------------------------------------------
# SYMSPELL TESTS (Ukrainian)
# ------------------------------------------------------------
@pytest.mark.skipif(not SYM_AVAILABLE, reason="SymSpell not installed")
def test_ukrainian_detection():
    assert UKRAINIAN_CHARS.search("привіт")

@pytest.mark.skipif(not SYM_AVAILABLE, reason="SymSpell not installed")
def test_symspell_ukrainian_correction(monkeypatch):
    monkeypatch.setattr("spelling.auto_correct", lambda w: "привіт")
    result = spelling.auto_correct("привт")
    assert result == "привіт"

@pytest.mark.skipif(not SYM_AVAILABLE, reason="SymSpell not installed")
def test_symspell_not_used_for_english():
    result = auto_correct("heelo")
    if not LANGUAGE_TOOL_AVAILABLE:
        assert result == "hello"


# SPELLING + DICTIONARY TESTS
# --- DICTIONARY SEARCH TESTS WITHOUT GUI ---

# Dummy replacement for Tkinter Entry widget
class DummyEntry:
    def __init__(self, value: str):
        self.value = value

    def get(self):
        return self.value

    def delete(self, start, end=None):
        self.value = ""

    def insert(self, index, new_text):
        self.value = new_text


# Dummy for Tkinter Variable (StringVar)
class DummyVar:
    def __init__(self, value: str):
        self.value = value

    def get(self):
        return self.value


class DummyApp:
    """
    Minimal stub to test dict_search without GUI.
    """
    dict_page: int
    dict_search_entry: DummyEntry
    dict_page_size_var: DummyVar
    last_loaded: dict
    dict_search: Callable[..., None]

    def __init__(self):
        self.dict_page = 0
        self.last_loaded = {}

    def load_dictionary_page(self, *args, **kwargs):
        # If a word was passed, it will be the first positional argument
        word = args[0] if args else None

        self.last_loaded = {
            "word": word,
            "order": kwargs.get("order_by", "word"),
            "limit": kwargs.get("limit", 20),
            "offset": kwargs.get("offset", 0),
        }


def test_dictionary_search_uses_corrected_word(monkeypatch):
    from admin_panel import AdminPanel

    dummy = DummyApp()
    dummy.dict_search_entry = DummyEntry("I hav a appel")
    dummy.dict_page_size_var = DummyVar("20")

    monkeypatch.setattr("spelling.auto_correct", lambda w: "I have an apple")

    # Bind AdminPanel.dict_search → dummy instance
    dummy.dict_search = AdminPanel.dict_search.__get__(dummy, DummyApp)
    dummy.dict_search()
    assert dummy.last_loaded["word"] == monkeypatch.setattr("spelling.auto_correct", lambda w: "I have an apple")
