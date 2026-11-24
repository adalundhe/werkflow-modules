from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PolicyApplicationViolation(BaseModel):
    entityId: StrictStr | None = None
    entityName: StrictStr | None = None
    entityType: StrictStr | None = None
    remediationHint: StrictStr | None = None
    ruleTypeId: StrictStr | None = None
