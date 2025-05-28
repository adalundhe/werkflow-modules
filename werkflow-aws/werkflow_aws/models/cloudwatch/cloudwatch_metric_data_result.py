import datetime
from pydantic import BaseModel, StrictStr, StrictInt
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
    Value: list[StrictInt]
    StatusCode: CloudWatchMetricDataResultStatusCode
    Messages: list[CloudWatchMessage] | None =None
