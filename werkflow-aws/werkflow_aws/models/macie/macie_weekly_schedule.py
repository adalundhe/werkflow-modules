from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieWeeklySchedule(BaseModel):
    dayOfWeek: StrictStr | None = None
