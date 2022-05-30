"""Custom client handling, including PercevalStream base class."""
import json
import os
from typing import Optional, Iterable

from singer_sdk.streams import Stream


class PercevalStream(Stream):
    """Stream class for PPEL streams."""

    #  The name of the value in the stream data (e.g. 'amount' for the total amount in €, 'count'
    #  for the total number) -> to be overridden by the actual Stream class
    metric_name = "metric"

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects."""
        file_path = self.config["file_path"]
        if not os.path.exists(file_path):
            raise Exception(f"File path does not exist {file_path}")

        with open(file_path) as f:
            all_data = json.load(f)

        # Stream-specific data, e.g. 'age_cat_month'
        stream_data = all_data[self.name]

        if len(self.primary_keys) == 1:
            # Example stream_data:
            # {
            #   "2019-11-30": 1,
            #   "2019-11-31": 2,
            # }
            key_name = self.primary_keys[0]
            for k, v in stream_data.items():
                yield {key_name: k, self.metric_name: v}

        elif len(self.primary_keys) == 2:
            # Example stream_data:
            # {
            #   "2019-11": {
            #     "00": 0,
            #     "15-24": 1,
            #     "25-34": 2,
            #     "35-44": 3,
            #     "45-54": 4,
            #     "55-64": 5,
            #     "65-74": 6,
            #     "75+": 0
            #     }
            # }
            key1_name, key2_name = self.primary_keys
            for k1, d in stream_data.items():
                for k2, v in d.items():
                    yield {key1_name: k1, key2_name: k2, self.metric_name: v}
