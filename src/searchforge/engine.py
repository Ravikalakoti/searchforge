"""
Main Search Engine implementation.
"""

from .normalizer import Normalizer
from .tokenizer import Tokenizer
from .stopwords import StopWords
from .index import InvertedIndex
from .query import QueryProcessor
from .ranking import TFIDFRanker
from .storage import JSONStorage


class SearchEngine:
    """
    High level search interface.

    Handles:
    - Document indexing
    - Query processing
    - Ranking
    - Persistence
    """

    def __init__(
        self,
        storage_path: str = "searchforge.json",
    ):
        self.normalizer = Normalizer()
        self.tokenizer = Tokenizer()
        self.stopwords = StopWords()

        self.index = InvertedIndex()

        self.query_processor = QueryProcessor()

        self.ranker = TFIDFRanker()

        self.documents = {}

        self.storage = JSONStorage(
            storage_path
        )


    def add_document(
        self,
        document_id: int,
        text: str,
    ) -> None:
        """
        Add document into search engine.
        """

        cleaned_text = self.normalizer.normalize(
            text
        )

        tokens = self.tokenizer.tokenize(
            cleaned_text
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

        if not query_tokens:
            return []


        matched_ids = set()


        for token in query_tokens:
            matched_ids.update(
                self.index.search(token)
            )


        matched_documents = {
            doc_id: self.documents[doc_id]
            for doc_id in matched_ids
        }


        return self.ranker.rank(
            query_tokens,
            matched_documents
        )


    def save(self) -> None:
        """
        Save documents to storage.
        """

        self.storage.save(
            self.documents
        )


    def load(self) -> None:
        """
        Load documents and rebuild index.
        """

        loaded_documents = self.storage.load()


        self.documents = {
            int(doc_id): tokens
            for doc_id, tokens in loaded_documents.items()
        }


        self.index.clear()


        for doc_id, tokens in self.documents.items():

            self.index.add_document(
                doc_id,
                tokens
            )
