from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSDnsDuplicateRuleGroupViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    ViolationTargetDescription: StrictStr | None = None
