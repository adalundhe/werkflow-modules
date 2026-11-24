from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ElastiCacheTimeRangeFilter(BaseModel):
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
