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
from .highlight import Highlighter
from .fuzzy import FuzzyMatcher
from .suggest import SuggestionEngine
from .analytics import SearchAnalytics
from .index_storage import IndexStorage
from .analytics_storage import AnalyticsStorage


class SearchEngine:
    """
    High level search engine.

    Features:
    - Document indexing
    - Metadata filtering
    - Ranking
    - Persistence
    - Highlighting
    - Fuzzy search
    - Autocomplete
    """


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

        self.highlighter = Highlighter()

        self.fuzzy = FuzzyMatcher()

        self.suggester = SuggestionEngine()

        self.analytics = SearchAnalytics()
        self.index_storage = IndexStorage()
        self.analytics_storage = AnalyticsStorage()

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


        # add words for autocomplete

        for token in tokens:

            self.suggester.add(
                token
            )


    def search(
        self,
        query: str,
        limit: int = 10,
        offset: int = 0,
        filters: dict | None = None,
    ) -> list[SearchResult]:
        """
        Search documents.
        """


        query_tokens = self.query_processor.process(
            query
        )

        self.analytics.track(
            query
        )

        self.analytics_storage.save(
            dict(self.analytics.queries)
        )

        if not query_tokens:
            return []



        matched_ids = set()



        for token in query_tokens:


            ids = self.index.search(
                token
            )


            # fuzzy fallback

            if not ids:

                all_words = list(
                    self.index.index.keys()
                )


                similar_words = self.fuzzy.match(
                    token,
                    all_words
                )


                for word in similar_words:

                    ids.update(
                        self.index.search(word)
                    )


            matched_ids.update(
                ids
            )



        matched_documents = {}



        for doc_id in matched_ids:


            document = self.documents[doc_id]



            if filters:


                matched = all(

                    document.metadata.get(key)
                    == value

                    for key, value
                    in filters.items()

                )


                if not matched:
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


            text = " ".join(
                document.content
            )


            highlight = self.highlighter.highlight(
                text,
                query_tokens
            )



            results.append(

                SearchResult(

                    document_id=doc_id,

                    score=score,

                    content=document.content,

                    metadata=document.metadata,

                    highlight=highlight,

                )

            )



        return results[
            offset:
            offset + limit
        ]



    def suggest(
        self,
        prefix: str,
        limit: int = 5,
    ) -> list[str]:
        """
        Return autocomplete suggestions.
        """

        return self.suggester.suggest(
            prefix,
            limit
        )



    def save(self) -> None:
        """
        Save documents.
        """

        data = {}


        for doc_id, document in self.documents.items():

            data[doc_id] = {

                "content": document.content,

                "metadata": document.metadata,

            }


        self.storage.save(
            data
        )

        self.index_storage.save(
            dict(self.index.index)
        )



    def load(self) -> None:
        """
        Load documents and restore index.
        """

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


            # restore autocomplete

            for token in document.content:

                self.suggester.add(
                    token
                )


        # restore persistent index

        stored_index = self.index_storage.load()


        if stored_index:

            for token, docs in stored_index.items():

                self.index.index[token] = {

                    int(doc_id): count

                    for doc_id, count in docs.items()

                }

        else:

            # fallback: rebuild index if index file missing

            for doc_id, document in self.documents.items():

                self.index.add_document(

                    doc_id,

                    document.content

                )

    def popular_queries(
        self,
        limit: int = 10,
    ):
        """
        Return popular search queries.
        """

        stored = self.analytics_storage.load()


        for query, count in stored.items():

            self.analytics.queries[query] = count


        return self.analytics.popular_queries(
            limit
        )
