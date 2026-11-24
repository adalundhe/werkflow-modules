from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MacieMonthlySchedule(BaseModel):
    dayOfMonth: StrictInt | None = None
