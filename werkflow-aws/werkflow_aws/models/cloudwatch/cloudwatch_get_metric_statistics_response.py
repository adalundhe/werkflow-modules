from pydantic import BaseModel, StrictStr
from .cloudwatch_datapoint import CloudWatchDatapoint


class CloudWatchGetMetricStatisticsResponse(BaseModel):
    Label: StrictStr
    Datapoints: list[CloudWatchDatapoint]
    