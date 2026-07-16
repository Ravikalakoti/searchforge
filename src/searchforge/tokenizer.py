"""
Tokenizer module.

Responsible for converting raw text into clean searchable tokens.
"""

import re
import unicodedata


class Tokenizer:
    """
    Converts text into normalized tokens.

    Example:
        Input:
            "Hello, Django Developer!"

        Output:
            ["hello", "django", "developer"]
    """

    def __init__(self, lowercase: bool = True):
        """
        Initialize tokenizer.

        Args:
            lowercase:
                Convert tokens to lowercase if True.
        """
        self.lowercase = lowercase

        # Match words and numbers
        self.pattern = re.compile(r"\b[a-zA-Z0-9]+\b")

    def normalize_unicode(self, text: str) -> str:
        """
        Normalize unicode characters.
        """
        return unicodedata.normalize("NFKC", text)

    def tokenize(self, text: str) -> list[str]:
        """
        Convert text into tokens.

        Args:
            text:
                Input text.

        Returns:
            List of tokens.
        """

        if not isinstance(text, str):
            raise TypeError("Tokenizer expects string input")

        # Unicode normalization
        text = self.normalize_unicode(text)

        # Lowercase
        if self.lowercase:
            text = text.lower()

        # Extract words
        tokens = self.pattern.findall(text)

        return tokens
