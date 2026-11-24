from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_scan_condition import GuardDutyScanCondition


class GuardDutyScanResourceCriteria(BaseModel):
    Include: dict[StrictStr, GuardDutyScanCondition] | None = None
    Exclude: dict[StrictStr, GuardDutyScanCondition] | None = None
