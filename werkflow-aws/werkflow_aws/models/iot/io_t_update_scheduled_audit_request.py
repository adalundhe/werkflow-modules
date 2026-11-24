from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTUpdateScheduledAuditRequest(BaseModel):
    scheduledAuditName: StrictStr
    frequency: Literal['DAILY', 'WEEKLY', 'BIWEEKLY', 'MONTHLY'] | None = None
    dayOfMonth: StrictStr | None = None
    dayOfWeek: Literal['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] | None = None
    targetCheckNames: list[StrictStr] | None = None
