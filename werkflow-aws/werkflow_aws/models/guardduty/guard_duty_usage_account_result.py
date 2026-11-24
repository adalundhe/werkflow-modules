from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_total import GuardDutyTotal


class GuardDutyUsageAccountResult(BaseModel):
    AccountId: StrictStr | None = None
    Total: GuardDutyTotal | None = None
