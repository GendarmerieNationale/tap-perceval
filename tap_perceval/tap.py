"""Perceval tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_perceval.streams import (
    AgeCatMonthStream,
    DailyCountStream,
    DptReportMonthStream,
    DailyAmountStream,
)


class TapPerceval(Tap):
    """Perceval tap class."""

    name = "tap-perceval"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "file_path",
            th.StringType,
            required=True,
            description="The absolute or relative path to the .json file with Perceval data",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [
            AgeCatMonthStream(tap=self),
            DailyAmountStream(tap=self),
            DptReportMonthStream(tap=self),
            DailyCountStream(tap=self),
        ]
