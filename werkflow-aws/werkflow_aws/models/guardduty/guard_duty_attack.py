from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_finding_reference import GuardDutyFindingReference
from .guard_duty_threat_reference import GuardDutyThreatReference


class GuardDutyAttack(BaseModel):
    Tactic: GuardDutyThreatReference | None = None
    Technique: GuardDutyThreatReference | None = None
    Findings: list[GuardDutyFindingReference] | None = None
    Version: StrictStr | None = None
