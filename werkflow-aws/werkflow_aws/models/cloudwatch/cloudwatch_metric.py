from pydantic import BaseModel, StrictStr
from .cloudwatch_dimension import CloudWatchDimension


class CloudWatchMetric(BaseModel):
    MetricName: StrictStr
    Namespace: StrictStr
    Dimensions: list[CloudWatchDimension] | None = None
