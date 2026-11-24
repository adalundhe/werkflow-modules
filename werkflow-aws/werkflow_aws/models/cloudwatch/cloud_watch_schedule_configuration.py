from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchScheduleConfiguration(BaseModel):
    ScheduleExpression: StrictStr | None = None
    StartTimeOffset: StrictInt | None = None
    EndTimeOffset: StrictInt | None = None
