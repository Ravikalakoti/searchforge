from searchforge.highlight import Highlighter


def test_highlight_text():

    highlighter = Highlighter()


    result = highlighter.highlight(
        "Django Python Developer",
        [
            "python"
        ]
    )


    assert (
        "<b>Python</b>"
        in result
    )
