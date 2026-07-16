from searchforge.engine import SearchEngine


def test_engine_save_load(tmp_path):

    engine = SearchEngine()

    engine.storage.path = (
        tmp_path / "search.json"
    )

    engine.add_document(
        1,
        "Django Python Developer"
    )

    engine.save()


    new_engine = SearchEngine()

    new_engine.storage.path = (
        tmp_path / "search.json"
    )

    new_engine.load()


    result = new_engine.search(
        "python"
    )

    assert result[0][0] == 1


