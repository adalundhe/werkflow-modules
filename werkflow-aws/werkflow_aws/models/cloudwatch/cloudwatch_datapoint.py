import datetime
from pydantic import BaseModel, StrictFloat, StrictStr
from .cloudwatch_unit import CloudWatchUnit


class CloudWatchDatapoint(BaseModel):
    Timestamp: datetime.datetime
    SampleCount: StrictFloat | None = None
    Average: StrictFloat | None = None
    Sum: StrictFloat | None = None
    Minimum: StrictFloat | None = None
    Maximum: StrictFloat | None = None
    Unit: CloudWatchUnit | None = None
    ExtendedStatistics: dict[StrictStr, StrictFloat] | None = None
