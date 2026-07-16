"""
Main Search Engine implementation.
"""

from .normalizer import Normalizer
from .tokenizer import Tokenizer
from .stopwords import StopWords
from .index import InvertedIndex
from .query import QueryProcessor
from .ranking import TFIDFRanker


class SearchEngine:
    """
    High level search interface.
    """

    def __init__(self):

        self.normalizer = Normalizer()
        self.tokenizer = Tokenizer()
        self.stopwords = StopWords()

        self.index = InvertedIndex()
        self.query_processor = QueryProcessor()

        self.ranker = TFIDFRanker()

        self.documents = {}

    def add_document(
        self,
        document_id: int,
        text: str,
    ) -> None:
        """
        Add document into search engine.
        """

        cleaned = self.normalizer.normalize(text)

        tokens = self.tokenizer.tokenize(
            cleaned
        )

        tokens = self.stopwords.remove(
            tokens
        )

        self.documents[document_id] = tokens

        self.index.add_document(
            document_id,
            tokens
        )


    def search(
        self,
        query: str,
    ) -> list[tuple[int, float]]:
        """
        Search documents and rank results.
        """

        query_tokens = self.query_processor.process(
            query
        )

        matched_documents = {}

        for doc_id in self.index.search(
            query_tokens[0]
        ):
            matched_documents[doc_id] = (
                self.documents[doc_id]
            )

        return self.ranker.rank(
            query_tokens,
            matched_documents
        )
