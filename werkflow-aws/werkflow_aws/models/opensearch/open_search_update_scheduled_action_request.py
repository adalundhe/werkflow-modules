from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchUpdateScheduledActionRequest(BaseModel):
    DomainName: StrictStr
    ActionID: StrictStr
    ActionType: Literal['SERVICE_SOFTWARE_UPDATE', 'JVM_HEAP_SIZE_TUNING', 'JVM_YOUNG_GEN_TUNING']
    ScheduleAt: Literal['NOW', 'TIMESTAMP', 'OFF_PEAK_WINDOW']
    DesiredStartTime: StrictInt | None = None
