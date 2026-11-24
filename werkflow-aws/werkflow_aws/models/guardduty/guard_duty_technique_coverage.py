from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_threat_reference import GuardDutyThreatReference


class GuardDutyTechniqueCoverage(BaseModel):
    Technique: GuardDutyThreatReference | None = None
    FindingCount: StrictInt | None = None
    FindingTypes: list[StrictStr] | None = None
