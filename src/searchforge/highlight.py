"""
Text highlighting utilities.
"""


class Highlighter:
    """
    Adds highlight markers around matched terms.
    """


    def highlight(
        self,
        text: str,
        terms: list[str],
    ) -> str:
        """
        Highlight matched words.

        Example:

        Input:
            "Django Python Developer"

        Terms:
            ["python"]

        Output:
            "Django <b>Python</b> Developer"
        """

        highlighted_text = text


        for term in terms:

            highlighted_text = (
                highlighted_text
                .replace(
                    term,
                    f"<b>{term}</b>"
                )
                .replace(
                    term.capitalize(),
                    f"<b>{term.capitalize()}</b>"
                )
            )


        return highlighted_text
