from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_attack_phase import GuardDutyAttackPhase


class GuardDutyThreatAssessment(BaseModel):
    AttackProgression: list[GuardDutyAttackPhase] | None = None
    ThreatActorProfile: StrictStr | None = None
