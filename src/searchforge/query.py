"""
Query processing module.
"""

from .normalizer import Normalizer
from .tokenizer import Tokenizer
from .stopwords import StopWords


class QueryProcessor:
    """
    Converts raw search query into clean tokens.
    """

    def __init__(self):
        self.normalizer = Normalizer()
        self.tokenizer = Tokenizer()
        self.stopwords = StopWords()

    def process(self, query: str) -> list[str]:
        """
        Process user query.

        Example:

        Input:
            "How to build Django API"

        Output:
            ["build", "django", "api"]
        """

        cleaned_text = self.normalizer.normalize(query)

        tokens = self.tokenizer.tokenize(
            cleaned_text
        )

        tokens = self.stopwords.remove(tokens)

        return tokens
