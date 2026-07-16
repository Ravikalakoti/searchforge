from searchforge.fuzzy import FuzzyMatcher


def test_fuzzy_match():

    matcher = FuzzyMatcher()


    result = matcher.match(
        "pyhton",
        [
            "python",
            "django",
            "java"
        ]
    )


    assert "python" in result
