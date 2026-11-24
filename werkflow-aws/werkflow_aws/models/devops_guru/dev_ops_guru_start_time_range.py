from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DevOpsGuruStartTimeRange(BaseModel):
    FromTime: datetime.datetime | StrictStr | None = None
    ToTime: datetime.datetime | StrictStr | None = None
