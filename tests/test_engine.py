from searchforge.engine import SearchEngine
from searchforge.results import SearchResult


def test_search_engine():

    engine = SearchEngine()

    engine.add_document(
        1,
        "Django Python Developer"
    )

    engine.add_document(
        2,
        "Python Web Framework"
    )

    result = engine.search(
        "python"
    )

    assert result[0].document_id in [1, 2]


def test_engine_save_load(tmp_path):

    engine = SearchEngine()

    engine.storage.path = (
        tmp_path / "search.json"
    )

    engine.add_document(
        1,
        "Django Python Developer"
    )

    engine.save()


    new_engine = SearchEngine()

    new_engine.storage.path = (
        tmp_path / "search.json"
    )

    new_engine.load()


    result = new_engine.search(
        "python"
    )

    assert result[0].document_id == 1



def test_search_result_object():

    engine = SearchEngine()


    engine.add_document(
        1,
        "Python Django Developer"
    )

    results = engine.search(
        "python"
    )


    assert isinstance(
        results[0],
        SearchResult
    )


    assert results[0].document_id == 1


def test_fuzzy_search():

    engine = SearchEngine()

    engine.add_document(
        1,
        "Python Django Developer"
    )

    results = engine.search(
        "pyhton"
    )

    assert results[0].document_id == 1


def test_engine_suggest():

    engine = SearchEngine()


    engine.add_document(
        1,
        "Python Django Developer"
    )


    results = engine.suggest(
        "py"
    )


    assert "python" in results


def test_search_analytics():

    engine = SearchEngine()


    engine.add_document(
        1,
        "Python Django Developer"
    )


    engine.search(
        "python"
    )


    engine.search(
        "python"
    )


    result = engine.popular_queries()


    assert result[0][0] == "python"

    assert result[0][1] == 2
