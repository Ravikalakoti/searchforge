"""
Ranking algorithms for search results.

Currently implements TF-IDF based ranking.
"""

import math
from collections import Counter


class TFIDFRanker:
    """
    Ranks documents using TF-IDF score.
    """

    def term_frequency(
        self,
        term: str,
        document: list[str],
    ) -> float:
        """
        Calculate how frequently term appears
        in a document.
        """

        if not document:
            return 0.0

        count = document.count(term)

        return count / len(document)


    def inverse_document_frequency(
        self,
        term: str,
        documents: dict[int, list[str]],
    ) -> float:
        """
        Calculate IDF score with smoothing.
        """

        total_documents = len(documents)

        matching_documents = sum(
            1
            for doc in documents.values()
            if term in doc
        )

        return math.log(
            (total_documents + 1)
            /
            (matching_documents + 1)
        ) + 1

    def score(
        self,
        query: list[str],
        document: list[str],
        documents: dict[int, list[str]],
    ) -> float:
        """
        Calculate document relevance score.
        """

        total_score = 0.0

        for term in query:

            tf = self.term_frequency(
                term,
                document
            )

            idf = self.inverse_document_frequency(
                term,
                documents
            )

            total_score += tf * idf

        return total_score

    def rank(
        self,
        query: list[str],
        documents: dict[int, list[str]],
    ) -> list[tuple[int, float]]:
        """
        Return documents sorted by relevance.
        """

        results = []

        for doc_id, content in documents.items():

            score = self.score(
                query,
                content,
                documents
            )

            results.append(
                (doc_id, score)
            )

        return sorted(
            results,
            key=lambda x: x[1],
            reverse=True,
        )
