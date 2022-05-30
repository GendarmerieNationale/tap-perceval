"""Stream type classes for tap-perceval."""

from singer_sdk import typing as th  # JSON Schema typing helpers
from tap_perceval.client import PercevalStream


class AgeCatMonthStream(PercevalStream):
    name = "age_categories_month"
    primary_keys = ["month", "age_cat"]
    metric_name = "count"
    replication_key = None

    schema = th.PropertiesList(
        th.Property("month", th.StringType),
        th.Property(
            "age_cat",
            th.StringType,
            description="The age category of the person reporting a fraud to Perceval",
        ),
        th.Property(
            "count",
            th.IntegerType,
            description="The total number of reports sent to Perceval, in this category, over the month",
        ),
    ).to_dict()


class DailyAmountStream(PercevalStream):
    name = "amount_of_money_day"
    primary_keys = ["day"]
    metric_name = "amount"
    replication_key = None

    schema = th.PropertiesList(
        th.Property("day", th.StringType),
        th.Property("amount", th.NumberType),
    ).to_dict()


class DptReportMonthStream(PercevalStream):
    name = "dpt_report_month"
    primary_keys = ["month", "dpt_code"]
    metric_name = "count"
    replication_key = None

    schema = th.PropertiesList(
        th.Property("month", th.StringType),
        th.Property("dpt_code", th.StringType),
        th.Property("count", th.IntegerType),
    ).to_dict()


class DailyCountStream(PercevalStream):
    name = "nb_report_day"
    primary_keys = ["day"]
    metric_name = "count"
    replication_key = None

    schema = th.PropertiesList(
        th.Property("day", th.StringType),
        th.Property("count", th.IntegerType),
    ).to_dict()
