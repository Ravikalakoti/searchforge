from searchforge.engine import SearchEngine


def test_search_engine():

    engine = SearchEngine()

    engine.add_document(
        1,
        "Django Python Developer"
    )

    engine.add_document(
        2,
        "Python Web Framework"
    )

    result = engine.search(
        "python"
    )

    assert result[0][0] in [1,2]
