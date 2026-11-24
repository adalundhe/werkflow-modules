from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .guard_duty_finding_type_classification import GuardDutyFindingTypeClassification


class GuardDutyBaseline(BaseModel):
    TotalFindings: StrictInt | None = None
    BaselineFindings: list[GuardDutyFindingTypeClassification] | None = None
    AnomalousFindings: list[GuardDutyFindingTypeClassification] | None = None
