"""
Ranking algorithms for search results.

Supports:
- TF-IDF
- BM25 style ranking
"""

import math
from collections import Counter



class TFIDFRanker:
    """
    TF-IDF based ranking.
    """



    def term_frequency(
        self,
        term: str,
        document: list[str],
    ) -> float:

        if not document:
            return 0.0


        frequency = document.count(
            term
        )


        return frequency / len(document)



    def inverse_document_frequency(
        self,
        term: str,
        documents: dict[int, list[str]],
    ) -> float:

        total_documents = len(
            documents
        )


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

        score = 0.0


        for term in query:


            tf = self.term_frequency(
                term,
                document
            )


            idf = self.inverse_document_frequency(
                term,
                documents
            )


            score += tf * idf


        return score



    def bm25_score(
        self,
        query: list[str],
        document: list[str],
        documents: dict[int, list[str]],
        k1: float = 1.5,
        b: float = 0.75,
    ) -> float:
        """
        BM25 ranking algorithm.
        """


        if not document:
            return 0.0


        score = 0.0


        document_length = len(
            document
        )


        average_length = (

            sum(
                len(doc)
                for doc in documents.values()
            )

            /

            len(documents)

        )


        frequency = Counter(
            document
        )



        for term in query:


            tf = frequency.get(
                term,
                0
            )


            if tf == 0:
                continue



            df = sum(

                1

                for doc in documents.values()

                if term in doc

            )


            idf = math.log(

                (

                    len(documents)
                    -
                    df
                    +
                    0.5

                )

                /

                (

                    df
                    +
                    0.5

                )

                +

                1

            )



            numerator = (

                tf
                *
                (k1 + 1)

            )


            denominator = (

                tf

                +

                k1
                *
                (

                    1
                    -
                    b

                    +

                    b
                    *
                    (
                        document_length
                        /
                        average_length
                    )

                )

            )


            score += (

                idf
                *
                numerator
                /
                denominator

            )


        return score



    def rank(
        self,
        query: list[str],
        documents: dict[int, list[str]],
    ) -> list[tuple[int, float]]:
        """
        Rank documents using BM25.
        """


        results = []


        for doc_id, content in documents.items():


            score = self.bm25_score(

                query,

                content,

                documents

            )


            results.append(

                (
                    doc_id,
                    score
                )

            )


        return sorted(

            results,

            key=lambda x: x[1],

            reverse=True,

        )
