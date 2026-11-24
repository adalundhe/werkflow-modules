from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_technique_coverage import GuardDutyTechniqueCoverage


class GuardDutyTacticCoverage(BaseModel):
    Phase: StrictStr | None = None
    FindingCount: StrictInt | None = None
    FindingTypes: list[StrictStr] | None = None
    Techniques: list[GuardDutyTechniqueCoverage] | None = None
