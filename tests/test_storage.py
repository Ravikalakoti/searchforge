from searchforge.storage import JSONStorage


def test_json_storage(tmp_path):

    file_path = tmp_path / "data.json"

    storage = JSONStorage(
        str(file_path)
    )

    data = {
        "1": [
            "python",
            "django",
        ]
    }

    storage.save(data)

    result = storage.load()

    assert result == data
