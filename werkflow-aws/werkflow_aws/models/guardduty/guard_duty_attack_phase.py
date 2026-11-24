from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_attack import GuardDutyAttack


class GuardDutyAttackPhase(BaseModel):
    Phase: StrictStr | None = None
    Description: StrictStr | None = None
    Attacks: list[GuardDutyAttack] | None = None
