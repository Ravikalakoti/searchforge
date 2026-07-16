from searchforge.index import InvertedIndex


def test_add_and_search_document():
    index = InvertedIndex()

    index.add_document(
        1,
        [
            "django",
            "python",
        ],
    )

    index.add_document(
        2,
        [
            "python",
        ],
    )

    assert index.search("python") == {1, 2}

    assert index.search("django") == {1}


def test_remove_document():
    index = InvertedIndex()

    index.add_document(
        1,
        [
            "python",
        ],
    )

    index.remove_document(1)

    assert index.search("python") == set()


def test_clear_index():
    index = InvertedIndex()

    index.add_document(
        1,
        [
            "django",
        ],
    )

    index.clear()

    assert index.search("django") == set()
