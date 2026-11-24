from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_condition import GuardDutyCondition


class GuardDutyFindingCriteria(BaseModel):
    Criterion: dict[StrictStr, GuardDutyCondition] | None = None
