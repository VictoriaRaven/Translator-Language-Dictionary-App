import pytest
from unittest.mock import patch, MagicMock
from yourmodule.gui.history import HistoryWindow

@pytest.fixture
def mock_root():
    return MagicMock()

@pytest.fixture
def gui(mock_root):
    return HistoryWindow(mock_root, db_path=":memory:")

@patch("yourmodule.gui.history.query_history")
def test_refresh_history(mock_query, gui):
    # Mock returned rows
    mock_query.return_value = ([
        (1, "cat", "gato", 1, "timestamp")
    ], 1)

    gui.refresh_history()

    assert mock_query.called
    assert gui.table.insert.called

@patch("yourmodule.gui.history.export_history_json")
@patch("yourmodule.gui.history.filedialog.asksaveasfilename")
def test_export_json(mock_dialog, mock_export, gui):
    mock_dialog.return_value = "test.json"

    gui.export_json()

    mock_export.assert_called_with(gui.rows, "test.json")

@patch("yourmodule.gui.history.export_history_pdf")
@patch("yourmodule.gui.history.filedialog.asksaveasfilename")
def test_export_pdf(mock_dialog, mock_export, gui):
    mock_dialog.return_value = "test.pdf"

    gui.export_pdf()

    mock_export.assert_called()