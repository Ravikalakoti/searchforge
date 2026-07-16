from searchforge.stopwords import StopWords


def test_remove_stopwords():
    stopwords = StopWords()

    result = stopwords.remove(
        [
            "django",
            "is",
            "a",
            "framework",
        ]
    )

    assert result == [
        "django",
        "framework",
    ]


def test_custom_stopword_add():
    stopwords = StopWords()

    stopwords.add("django")

    assert stopwords.is_stopword("django")


def test_custom_remove():
    stopwords = StopWords()

    stopwords.add("django")
    stopwords.remove_word("django")

    assert not stopwords.is_stopword("django")
