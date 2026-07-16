from searchforge.analytics_storage import AnalyticsStorage



def test_analytics_storage(tmp_path):

    storage = AnalyticsStorage(
        tmp_path / "analytics.json"
    )


    storage.save(
        {
            "python": 2
        }
    )


    result = storage.load()


    assert result["python"] == 2
