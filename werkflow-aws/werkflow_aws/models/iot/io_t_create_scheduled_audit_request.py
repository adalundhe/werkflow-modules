from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag


class IoTCreateScheduledAuditRequest(BaseModel):
    frequency: Literal['DAILY', 'WEEKLY', 'BIWEEKLY', 'MONTHLY']
    targetCheckNames: list[StrictStr]
    scheduledAuditName: StrictStr
    dayOfMonth: StrictStr | None = None
    dayOfWeek: Literal['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] | None = None
    tags: list[IoTTag] | None = None
