"""
Index persistence storage.

Stores inverted index separately.
"""

import json
from pathlib import Path


class IndexStorage:
    """
    Stores and loads inverted index.
    """


    def __init__(
        self,
        path: str = "searchforge_index.json",
    ):

        self.path = Path(
            path
        )



    def save(
        self,
        index: dict,
    ) -> None:
        """
        Save index data.
        """


        with self.path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                index,
                file,
                indent=4,
            )



    def load(
        self,
    ) -> dict:
        """
        Load index data.
        """


        if not self.path.exists():

            return {}


        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(
                file
            )
