from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyFetchTimeWindow(BaseModel):
    StartedAt: datetime.datetime | StrictStr | None = None
    DurationInMinutes: StrictInt | None = None
