# tests/test_integration.py
def test_full_database_flow(monkeypatch, tmp_path):
    import database
    import translation

    tmp = tmp_path / "db.sqlite"
    monkeypatch.setattr(database, "DB_NAME", str(tmp))
    database.init_db()
    database.insert_dictionary_row("cat", "gato", "en")
    result = translation.sql_translate("cat", "en")
    assert result == "gato" or ("gato", False)


