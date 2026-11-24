from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2SlotDateTimeRangeRequest(BaseModel):
    EarliestTime: datetime.datetime | StrictStr
    LatestTime: datetime.datetime | StrictStr
