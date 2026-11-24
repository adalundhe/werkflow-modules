from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyActivityWindow(BaseModel):
    FirstSeenAt: datetime.datetime | StrictStr | None = None
    LastSeenAt: datetime.datetime | StrictStr | None = None
