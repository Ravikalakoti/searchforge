from searchforge.suggest import SuggestionEngine



def test_suggestion():

    engine = SuggestionEngine()


    engine.add(
        "python"
    )

    engine.add(
        "python django"
    )

    engine.add(
        "java"
    )


    result = engine.suggest(
        "py"
    )


    assert "python" in result
