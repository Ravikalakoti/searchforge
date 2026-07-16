"""
Document model.
"""

from dataclasses import dataclass, field


@dataclass
class Document:
    """
    Represents a searchable document.
    """

    document_id: int
    content: list[str]
    metadata: dict = field(default_factory=dict)
