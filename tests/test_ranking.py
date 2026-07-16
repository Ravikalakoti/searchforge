from searchforge.ranking import TFIDFRanker


def test_ranking_documents():

    ranker = TFIDFRanker()

    documents = {
        1: [
            "python",
            "python",
            "django",
        ],
        2: [
            "python",
            "developer",
        ],
    }

    result = ranker.rank(
        ["python"],
        documents,
    )

    assert result[0][0] == 1
