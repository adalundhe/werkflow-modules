from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DevOpsGuruEndTimeRange(BaseModel):
    FromTime: datetime.datetime | StrictStr | None = None
    ToTime: datetime.datetime | StrictStr | None = None
