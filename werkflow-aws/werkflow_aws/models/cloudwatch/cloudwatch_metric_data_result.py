import datetime
from pydantic import BaseModel, StrictStr, StrictFloat, StrictInt
from typing import Literal
from .cloudwatch_message import CloudWatchMessage


CloudWatchMetricDataResultStatusCode = Literal[
    "Complete",
    "InternalError",
    "PartialData",
    "Forbidden"
]


class CloudWatchMetricDataResult(BaseModel):
    Id: StrictStr
    Label: StrictStr
    Timestamps: list[datetime.datetime]
    Values: list[StrictInt | StrictFloat]
    StatusCode: CloudWatchMetricDataResultStatusCode
    Messages: list[CloudWatchMessage] | None =None
