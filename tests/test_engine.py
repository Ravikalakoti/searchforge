from searchforge.engine import SearchEngine


def test_multi_word_search():

    engine = SearchEngine()

    engine.add_document(
        1,
        "Django Python Developer"
    )

    engine.add_document(
        2,
        "Java Developer"
    )

    result = engine.search(
        "Django Python"
    )

    assert result[0][0] == 1

