"""
Search result objects.
"""


from dataclasses import dataclass


@dataclass
class SearchResult:
    """
    Represents single search result.
    """

    document_id: int
    score: float
    content: list[str]
