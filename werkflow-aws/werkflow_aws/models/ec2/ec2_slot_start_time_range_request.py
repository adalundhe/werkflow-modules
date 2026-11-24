from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2SlotStartTimeRangeRequest(BaseModel):
    EarliestTime: datetime.datetime | StrictStr | None = None
    LatestTime: datetime.datetime | StrictStr | None = None
