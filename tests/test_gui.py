# inside tests/test_gui.py (replace the earlier online test)
from unittest.mock import patch
import gui
from translation import sql_translate, online_translate


@patch("gui.online_translate", autospec=True)
@patch("gui.save_history", autospec=True)
@patch("gui.sql_translate", autospec=True)
def test_online_translation_success(mock_sql, mock_save, mock_online_func, app, monkeypatch):
    # local miss
    mock_sql.return_value = (None, False)
    mock_online_func.return_value = "bonjour"

    monkeypatch.setattr(app, "use_online_var", app.use_online_var)
    monkeypatch.setattr(__import__("gui"), "threading", __import__("threading"))  # ensure threading exists
    # Replace Thread in gui module so start() runs target synchronously:
    class ImmediateThread:
        def __init__(self, target, args=(), daemon=None):
            self._target = target
            self._args = args
        def start(self):
            self._target(*self._args)
    monkeypatch.setattr("gui.threading.Thread", ImmediateThread)

    app.use_online_var.set(1)
    app.word_input.get = lambda index1="0.0", index2="end": "hello"
    app.lang_var.set(gui.LANG_OPTIONS[0][0])

    app.translate()

    # online_translate should have been called (we patched translation.online_translate)
    mock_online_func.assert_called_once()
    # And save_history should have been called for online result
    mock_save.assert_called()
