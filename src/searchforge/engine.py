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
from .results import SearchResult
from .document import Document


class SearchEngine:

    def __init__(
        self,
        storage_path="searchforge.json",
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
        metadata: dict | None = None,
    ) -> None:
        """
        Add document with metadata.
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


        document = Document(
            document_id=document_id,
            content=tokens,
            metadata=metadata or {},
        )


        self.documents[document_id] = document


        self.index.add_document(
            document_id,
            tokens
        )


    def search(
        self,
        query: str,
        limit: int = 10,
        offset: int = 0,
        filters: dict | None = None,
    ) -> list[SearchResult]:


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


        matched_documents = {}


        for doc_id in matched_ids:

            document = self.documents[doc_id]


            if filters:

                match = all(
                    document.metadata.get(key)
                    == value

                    for key, value
                    in filters.items()
                )

                if not match:
                    continue


            matched_documents[doc_id] = (
                document.content
            )


        ranked_results = self.ranker.rank(
            query_tokens,
            matched_documents
        )


        results = []


        for doc_id, score in ranked_results:

            document = self.documents[doc_id]


            results.append(
                SearchResult(
                    document_id=doc_id,
                    score=score,
                    content=document.content,
                    metadata=document.metadata,
                )
            )


        return results[
            offset:
            offset + limit
        ]


    def save(self):

        data = {}

        for doc_id, document in self.documents.items():

            data[doc_id] = {
                "content": document.content,
                "metadata": document.metadata,
            }


        self.storage.save(data)



    def load(self):

        loaded = self.storage.load()


        self.documents = {}


        self.index.clear()


        for doc_id, data in loaded.items():

            document = Document(
                document_id=int(doc_id),
                content=data["content"],
                metadata=data["metadata"],
            )


            self.documents[int(doc_id)] = document


            self.index.add_document(
                int(doc_id),
                document.content
            )
