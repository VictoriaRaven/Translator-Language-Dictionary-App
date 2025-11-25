from unittest.mock import MagicMock
import pytest
from gui import TranslatorApp
import gui
@pytest.fixture
def app(monkeypatch):
    """
    Fixture that creates the TranslatorApp in test mode.
    Tkinter is disabled using test_mode=True so windows do not open.
    """
    monkeypatch.setattr("tkinter.Tk", MagicMock())
    app = TranslatorApp(test_mode=True)
    #monkeypatch.setattr(app, "mainloop", lambda: None)
    print("DEBUG: gui imported from:", gui.__file__)
    return app


