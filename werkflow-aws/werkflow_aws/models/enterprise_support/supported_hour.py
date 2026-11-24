from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportedHour(BaseModel):
    startTime: StrictStr | None = None
    endTime: StrictStr | None = None
