from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SWFExecutionTimeFilter(BaseModel):
    oldestDate: datetime.datetime | StrictStr
    latestDate: datetime.datetime | StrictStr | None = None
