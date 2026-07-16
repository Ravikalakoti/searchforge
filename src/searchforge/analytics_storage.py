"""
Analytics persistence storage.
"""

import json
from pathlib import Path


class AnalyticsStorage:
    """
    Stores search analytics data.
    """


    def __init__(
        self,
        path: str = "searchforge_analytics.json",
    ):

        self.path = Path(path)



    def save(
        self,
        data: dict,
    ) -> None:
        """
        Save analytics.
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
        Load analytics.
        """

        if not self.path.exists():

            return {}


        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)
