from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FMSDnsRuleGroupLimitExceededViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    ViolationTargetDescription: StrictStr | None = None
    NumberOfRuleGroupsAlreadyAssociated: StrictInt | None = None
