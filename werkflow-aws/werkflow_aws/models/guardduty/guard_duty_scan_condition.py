from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_scan_condition_pair import GuardDutyScanConditionPair


class GuardDutyScanCondition(BaseModel):
    MapEquals: list[GuardDutyScanConditionPair] | None = None
