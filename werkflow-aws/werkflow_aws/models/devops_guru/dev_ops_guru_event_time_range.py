from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DevOpsGuruEventTimeRange(BaseModel):
    FromTime: datetime.datetime | StrictStr
    ToTime: datetime.datetime | StrictStr
