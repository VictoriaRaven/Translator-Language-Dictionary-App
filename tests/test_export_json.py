import json
import tempfile
from yourmodule.export import export_history_json

def test_export_history_json():
    rows = [
        (1, "cat", "gato", 0, "2025-11-24 10:00:00"),
        (2, "dog", "perro", 1, "2025-11-24 10:01:00"),
    ]

    path = tempfile.NamedTemporaryFile(delete=False, suffix=".json").name
    export_history_json(rows, path)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["word"] == "cat"