from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_total import GuardDutyTotal


class GuardDutyUsageResourceResult(BaseModel):
    Resource: StrictStr | None = None
    Total: GuardDutyTotal | None = None
