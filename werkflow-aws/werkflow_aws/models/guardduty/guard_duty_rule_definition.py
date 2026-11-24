from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyRuleDefinition(BaseModel):
    Expression: StrictStr | None = None
