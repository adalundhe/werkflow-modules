import datetime
from pydantic import BaseModel, StrictStr
from .cloudwatch_dimension import CloudWatchDimension
from .cloudwatch_statistics import CloudWatchStatistics
from .cloudwatch_unit import CloudWatchUnit


class CloudWatchGetMetricStatisticsRequest(BaseModel):
    Namespace: StrictStr
    MetricName: StrictStr
    Dimensions: list[CloudWatchDimension] | None = None
    StartTime: datetime.datetime
    EndTime: datetime.datetime
    Period: int
    Statistics: list[CloudWatchStatistics] | None = None
    ExtendedStatistics: list[StrictStr] | None = None
    Unit: CloudWatchUnit | None = None