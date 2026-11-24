from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchStartServiceSoftwareUpdateRequest(BaseModel):
    DomainName: StrictStr
    ScheduleAt: Literal['NOW', 'TIMESTAMP', 'OFF_PEAK_WINDOW'] | None = None
    DesiredStartTime: StrictInt | None = None
