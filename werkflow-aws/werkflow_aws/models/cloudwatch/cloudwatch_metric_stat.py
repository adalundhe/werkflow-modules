from pydantic import BaseModel, StrictStr, StrictInt
from .cloudwatch_metric import CloudWatchMetric
from .cloudwatch_statistics import CloudWatchStatistics
from .cloudwatch_unit import CloudWatchUnit


class CloudWatchMetricStat(BaseModel):
    Metric: CloudWatchMetric
    Period: StrictInt
    Stat: CloudWatchStatistics | StrictStr
    Unit: CloudWatchUnit | None = None
