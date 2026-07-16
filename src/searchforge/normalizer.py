"""
Text normalization utilities.

Responsible for cleaning raw text before tokenization.
"""

import re
import unicodedata


class Normalizer:
    """
    Cleans and normalizes text.

    Example:
        Input:
            "  Café Django!!!  "

        Output:
            "cafe django"
    """

    def __init__(self, lowercase: bool = True):
        self.lowercase = lowercase

    def normalize_unicode(self, text: str) -> str:
        """
        Convert unicode characters into standard form.
        """
        text = unicodedata.normalize("NFKD", text)

        # Remove accents
        return "".join(
            char
            for char in text
            if not unicodedata.combining(char)
        )

    def clean_spaces(self, text: str) -> str:
        """
        Remove extra spaces.
        """
        return re.sub(r"\s+", " ", text).strip()

    def remove_special_characters(self, text: str) -> str:
        """
        Remove unnecessary special characters.
        """
        return re.sub(
            r"[^a-zA-Z0-9\s]",
            "",
            text
        )

    def normalize(self, text: str) -> str:
        """
        Complete normalization pipeline.
        """

        if not isinstance(text, str):
            raise TypeError(
                "Normalizer expects string input"
            )

        text = self.normalize_unicode(text)

        text = self.remove_special_characters(text)

        text = self.clean_spaces(text)

        if self.lowercase:
            text = text.lower()

        return text
