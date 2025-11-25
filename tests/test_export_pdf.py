from unittest.mock import patch, MagicMock
import tempfile
from yourmodule.export import export_history_pdf

@patch("yourmodule.export.SimpleDocTemplate")
@patch("yourmodule.export.Paragraph")
@patch("yourmodule.export.pdfmetrics")
@patch("yourmodule.export.UnicodeCIDFont")
def test_export_history_pdf(mock_font, mock_metrics, mock_para, mock_template):
    rows = [
        (1, "cat", "gato", 0, "now"),
        (2, "dog", "perro", 1, "now"),
    ]

    mock_doc = MagicMock()
    mock_template.return_value = mock_doc

    path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    export_history_pdf(rows, path)

    mock_doc.build.assert_called()