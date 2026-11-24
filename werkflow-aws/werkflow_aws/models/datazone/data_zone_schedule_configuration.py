from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneScheduleConfiguration(BaseModel):
    timezone: StrictStr | None = None
    schedule: StrictStr | None = None
