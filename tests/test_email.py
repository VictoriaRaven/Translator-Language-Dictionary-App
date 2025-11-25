from unittest.mock import patch, MagicMock
from yourmodule.emailer import send_history_email
import webbrowser

@patch("yourmodule.emailer.Dispatch")
def test_send_history_email_outlook(mock_disp):
    mock_outlook = MagicMock()
    mock_disp.return_value = mock_outlook

    send_history_email("test@example.com", "Hello", "Body", attachment=None)

    mock_outlook.CreateItem.assert_called()

@patch("yourmodule.emailer.Dispatch", side_effect=Exception("Outlook not available"))
@patch("webbrowser.open")
def test_send_history_email_mailto(mock_open, mock_disp):
    send_history_email("test@example.com", "Hi", "Body", attachment=None)
    assert mock_open.called