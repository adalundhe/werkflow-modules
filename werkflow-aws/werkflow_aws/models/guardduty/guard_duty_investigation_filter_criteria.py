from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .guard_duty_investigation_filter_condition import GuardDutyInvestigationFilterCondition


class GuardDutyInvestigationFilterCriteria(BaseModel):
    Criterion: dict[Literal['STATUS', 'RISK_LEVEL', 'CONFIDENCE', 'FINDING_ID', 'INVESTIGATION_TYPE'], GuardDutyInvestigationFilterCondition] | None = None
