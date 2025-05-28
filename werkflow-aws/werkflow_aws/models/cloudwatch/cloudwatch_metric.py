from pydantic import BaseModel, StrictStr
from .cloudwatch_dimension import CloudWatchDimension


class CloudWatchMetric(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    Dimensions: list[CloudWatchDimension] | None = None
