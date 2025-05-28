import datetime
from pydantic import BaseModel, StrictFloat, StrictStr
from .cloudwatch_statistics import CloudWatchStatistics


class CloudWatchDatapoint(BaseModel):
    Timestamp: datetime.datetime
    SampleCount: StrictFloat | None = None
    Average: StrictFloat | None = None
    Sum: StrictFloat | None = None
    Minimum: StrictFloat | None = None
    Maximum: StrictFloat | None = None
    Unit: CloudWatchStatistics | None = None
    ExtendedStatistics: dict[StrictStr, StrictFloat] | None = None
