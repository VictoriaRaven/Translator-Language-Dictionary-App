import json
import tempfile
import os
from exports import export_history_json

def test_export_history_json():
    # rows must mimic real SQLite rows:
    # (id, input_word, output_word, language, used_online, timestamp)
    rows = [
        (1, "cat", "gato", "en", True, "2025-02-01 12:00:00"),
        (2, "dog", "perro", "en", False, "2025-02-01 12:05:00")
    ]

    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.close()

    export_history_json(tmp.name, rows)

    # Read JSON back
    with open(tmp.name, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 2

    assert data[0]["id"] == 1
    assert data[0]["input_word"] == "cat"
    assert data[0]["output_word"] == "gato"
    assert data[0]["language"] == "en"
    assert data[0]["used_online"] is True

    assert data[1]["id"] == 2
    assert data[1]["input_word"] == "dog"
    assert data[1]["output_word"] == "perro"
    assert data[1]["language"] == "en"
    assert data[1]["used_online"] is False

    os.unlink(tmp.name)
