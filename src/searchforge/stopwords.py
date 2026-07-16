"""
Stop words handler.

Removes common words that do not add much meaning
during search indexing and querying.
"""


class StopWords:
    """
    Manage stop words using fast set lookup.

    Example:
        "django is a framework"

        becomes:

        ["django", "framework"]
    """

    DEFAULT_WORDS = {
        "a",
        "an",
        "the",
        "is",
        "are",
        "was",
        "were",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "of",
        "with",
    }

    def __init__(self, words: set[str] | None = None):
        """
        Initialize stop words.

        Custom words replace default words.
        """

        self.words = (
            words
            if words is not None
            else self.DEFAULT_WORDS.copy()
        )

    def is_stopword(self, word: str) -> bool:
        """
        Check whether word is a stop word.
        """

        return word.lower() in self.words

    def remove(self, tokens: list[str]) -> list[str]:
        """
        Remove stop words from token list.
        """

        return [
            token
            for token in tokens
            if not self.is_stopword(token)
        ]

    def add(self, word: str) -> None:
        """
        Add custom stop word.
        """

        self.words.add(word.lower())

    def remove_word(self, word: str) -> None:
        """
        Remove word from stop word list.
        """

        self.words.discard(word.lower())
