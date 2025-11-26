import tempfile
from exports import export_history_pdf

def test_export_history_pdf_file_and_return():
    # Rows must match the tuple structure used by export_history_pdf:
    # earlier you used r[0], r[5], r[1], r[2], r[3], r[4]
    rows = [
        (1, "cat", "gato", 0, 1, "2025-11-24 10:00:00"),
        (2, "dog", "perro", 1, 0, "2025-11-24 10:01:00"),
    ]
    path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    ok, msg = export_history_pdf(path, rows)
    if not ok:
        print(f"[DEBUG] export_history_pdf failed with message: {msg}")
    
    # This assert ensures the test fails if ok is False
    assert ok is True, f"export_history_pdf returned False: {msg}"
