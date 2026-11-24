from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SchedulerFlexibleTimeWindow(BaseModel):
    Mode: StrictStr | None = None
    MaximumWindowInMinutes: StrictInt | None = None
