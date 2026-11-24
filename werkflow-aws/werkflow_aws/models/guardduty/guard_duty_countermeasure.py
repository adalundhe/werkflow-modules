from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_countermeasure_action import GuardDutyCountermeasureAction


class GuardDutyCountermeasure(BaseModel):
    DefenseTactic: StrictStr | None = None
    Actions: list[GuardDutyCountermeasureAction] | None = None
    Description: StrictStr | None = None
