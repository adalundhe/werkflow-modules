from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_correlated_finding import GuardDutyCorrelatedFinding
from .guard_duty_observed_finding_type import GuardDutyObservedFindingType


class GuardDutyRelatedFindings(BaseModel):
    Correlated: list[GuardDutyCorrelatedFinding] | None = None
    Observed: list[GuardDutyObservedFindingType] | None = None
