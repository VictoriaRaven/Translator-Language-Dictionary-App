import tempfile
from yourmodule.database import (
    init_db, insert_dictionary_row, query_dictionary, save_history, query_history
)
from yourmodule.translation import sql_translate

def test_full_database_flow():
    path = tempfile.NamedTemporaryFile(delete=False).name
    init_db(path)

    insert_dictionary_row(path, "cat", "gato", "en", "es")

    result = sql_translate(path, "cat")
    assert result == "gato"

    save_history(path, "cat", "gato", used_online=False)
    rows, total = query_history(path)

    assert total == 1
    assert rows[0][1] == "cat"
    assert rows[0][2] == "gato"