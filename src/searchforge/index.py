"""
Inverted index implementation.

Maps words/tokens to document IDs for fast search.
"""

from collections import defaultdict


class InvertedIndex:
    """
    Stores token to document mapping.

    Example:

    python -> {1, 2}
    django -> {1}
    """

    def __init__(self):
        self.index = defaultdict(set)

    def add_document(
        self,
        document_id: int,
        tokens: list[str],
    ) -> None:
        """
        Add document tokens into index.
        """

        for token in tokens:
            self.index[token].add(document_id)

    def remove_document(
        self,
        document_id: int,
    ) -> None:
        """
        Remove document from index.
        """

        for token in list(self.index.keys()):
            self.index[token].discard(document_id)

            # Remove empty tokens
            if not self.index[token]:
                del self.index[token]

    def search(
        self,
        token: str,
    ) -> set[int]:
        """
        Find documents containing token.
        """

        return self.index.get(
            token,
            set()
        )

    def clear(self) -> None:
        """
        Clear complete index.
        """

        self.index.clear()
