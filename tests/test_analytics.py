from searchforge.analytics import SearchAnalytics



def test_query_tracking():

    analytics = SearchAnalytics()


    analytics.track(
        "Python"
    )

    analytics.track(
        "python"
    )


    result = analytics.popular_queries()


    assert result[0][0] == "python"

    assert result[0][1] == 2
