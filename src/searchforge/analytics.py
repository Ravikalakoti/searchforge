"""
Search analytics module.
"""

from collections import Counter


class SearchAnalytics:
    """
    Tracks search queries.
    """


    def __init__(self):

        self.queries = Counter()



    def track(
        self,
        query: str,
    ) -> None:
        """
        Store search query.
        """

        query = query.lower().strip()


        if query:

            self.queries[query] += 1



    def popular_queries(
        self,
        limit: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Return most searched queries.
        """

        return self.queries.most_common(
            limit
        )



    def history(
        self,
    ) -> list[str]:
        """
        Return all searches.
        """

        return list(
            self.queries.keys()
        )
