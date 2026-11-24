from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FMSDnsRuleGroupPriorityConflictViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    ViolationTargetDescription: StrictStr | None = None
    ConflictingPriority: StrictInt | None = None
    ConflictingPolicyId: StrictStr | None = None
    UnavailablePriorities: list[StrictInt] | None = None
