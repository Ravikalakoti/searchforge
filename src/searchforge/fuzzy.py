"""
Fuzzy search utilities.
"""


def levenshtein_distance(
    first: str,
    second: str,
) -> int:
    """
    Calculate edit distance between two strings.
    """

    if len(first) < len(second):
        return levenshtein_distance(
            second,
            first
        )

    if len(second) == 0:
        return len(first)


    previous_row = range(
        len(second) + 1
    )


    for i, char1 in enumerate(first):

        current_row = [
            i + 1
        ]


        for j, char2 in enumerate(second):

            insert_cost = previous_row[j + 1] + 1

            delete_cost = current_row[j] + 1

            replace_cost = (
                previous_row[j]
                +
                (char1 != char2)
            )


            current_row.append(
                min(
                    insert_cost,
                    delete_cost,
                    replace_cost
                )
            )


        previous_row = current_row


    return previous_row[-1]


class FuzzyMatcher:
    """
    Finds similar words.
    """


    def __init__(
        self,
        threshold: int = 2,
    ):
        self.threshold = threshold


    def match(
        self,
        word: str,
        candidates: list[str],
    ) -> list[str]:
        """
        Return similar words.
        """

        matches = []


        for candidate in candidates:

            distance = levenshtein_distance(
                word,
                candidate
            )


            if distance <= self.threshold:

                matches.append(
                    candidate
                )


        return matches
