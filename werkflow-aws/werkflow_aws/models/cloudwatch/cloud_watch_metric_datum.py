from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .cloud_watch_statistic_set import CloudWatchStatisticSet
from .cloudwatch_dimension import CloudWatchDimension
from .cloudwatch_unit import CloudWatchUnit


class CloudWatchMetricDatum(BaseModel):
    MetricName: StrictStr | None = None
    Dimensions: list[CloudWatchDimension] | None = None
    Timestamp: datetime.datetime | None = None
    Value: StrictFloat | None = None
    StatisticValues: CloudWatchStatisticSet | None = None
    Values: list[StrictFloat] | None = None
    Counts: list[StrictFloat] | None = None
    Unit: CloudWatchUnit | None = None
    StorageResolution: StrictInt | None = None
