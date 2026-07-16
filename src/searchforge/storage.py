"""
Storage module.

Handles saving and loading search engine data.
"""

import json
from pathlib import Path


class JSONStorage:
    """
    Simple JSON based storage.
    """

    def __init__(self, path: str = "searchforge.json"):
        self.path = Path(path)

    def save(
        self,
        data: dict,
    ) -> None:
        """
        Save data into JSON file.
        """

        with self.path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
            )

    def load(self) -> dict:
        """
        Load data from JSON file.
        """

        if not self.path.exists():
            return {}

        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)
