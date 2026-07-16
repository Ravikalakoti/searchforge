"""
Search result objects.
"""

from dataclasses import dataclass


@dataclass
class SearchResult:

    document_id: int

    score: float

    content: list[str]

    metadata: dict

    highlight: str | None = None
