"""
Optimized inverted index implementation.

Stores token frequency per document.
"""

from collections import defaultdict, Counter


class InvertedIndex:
    """
    Stores token -> document frequency mapping.

    Example:

    python -> {
        1: 2,
        2: 1
    }
    """


    def __init__(self):

        self.index = defaultdict(dict)



    def add_document(
        self,
        document_id: int,
        tokens: list[str],
    ) -> None:
        """
        Add document tokens into index.
        """


        frequencies = Counter(
            tokens
        )


        for token, count in frequencies.items():

            self.index[token][
                document_id
            ] = count



    def remove_document(
        self,
        document_id: int,
    ) -> None:
        """
        Remove document from index.
        """


        for token in list(
            self.index.keys()
        ):


            self.index[token].pop(
                document_id,
                None
            )


            if not self.index[token]:

                del self.index[token]



    def search(
        self,
        token: str,
    ) -> set[int]:
        """
        Find documents containing token.
        """


        return set(
            self.index.get(
                token,
                {}
            ).keys()
        )



    def term_frequency(
        self,
        token: str,
        document_id: int,
    ) -> int:
        """
        Return token frequency in document.
        """


        return self.index.get(
            token,
            {}
        ).get(
            document_id,
            0
        )



    def document_frequency(
        self,
        token: str,
    ) -> int:
        """
        Number of documents containing token.
        """


        return len(
            self.index.get(
                token,
                {}
            )
        )



    def clear(self) -> None:
        """
        Clear index.
        """

        self.index.clear()
