from pydantic import BaseModel, StrictStr
from .cloudwatch_dimension import CloudWatchDimension


class CloudWatchMetric(BaseModel):
    Name: StrictStr
    Value: StrictStr
    Dimensions: list[CloudWatchDimension] | None = None
