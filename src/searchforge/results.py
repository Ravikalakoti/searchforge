"""
Search result objects.
"""

from dataclasses import dataclass


@dataclass
class SearchResult:
    """
    Represents a single search result.
    """

    document_id: int
    score: float
    content: list[str]
    metadata: dict
