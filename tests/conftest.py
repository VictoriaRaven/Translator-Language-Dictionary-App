from unittest.mock import MagicMock
import pytest
from gui import TranslatorApp

@pytest.fixture
def app(monkeypatch):
    """
    Fixture that creates the TranslatorApp in test mode.
    Tkinter is disabled using test_mode=True so windows do not open.
    """
    monkeypatch.setattr("gui.tk.Tk", MagicMock())
    app = TranslatorApp(test_mode=True)
    #monkeypatch.setattr(app, "mainloop", lambda: None)

    return app
