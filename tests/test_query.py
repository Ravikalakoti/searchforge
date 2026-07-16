from searchforge.query import QueryProcessor


def test_query_processing():

    processor = QueryProcessor()

    result = processor.process(
        "How to build Django API"
    )

    assert result == [
        "how",
        "build",
        "django",
        "api",
    ]
