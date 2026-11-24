from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointOpenHoursRule(BaseModel):
    StartTime: StrictStr | None = None
    EndTime: StrictStr | None = None
