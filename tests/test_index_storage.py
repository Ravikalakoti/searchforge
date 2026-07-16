from searchforge.index_storage import IndexStorage



def test_index_storage(tmp_path):

    storage = IndexStorage(
        tmp_path / "index.json"
    )


    data = {
        "python": {
            "1": 3
        }
    }


    storage.save(
        data
    )


    result = storage.load()


    assert result["python"]["1"] == 3
