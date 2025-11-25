import pytest
from __main__.validation import validate_input_word

def test_validate_input_word_valid():
    assert validate_input_word("hello") is True

def test_validate_input_word_accented():
    assert validate_input_word("café") is True

def test_validate_input_word_empty():
    assert validate_input_word("") is False

def test_validate_input_word_too_long():
    assert validate_input_word("a" * 201) is False

def test_validate_input_word_invalid_chars():
    assert validate_input_word("hi!!!") is False

def test_validate_input_word_emoji():
    assert validate_input_word("hello😊") is False