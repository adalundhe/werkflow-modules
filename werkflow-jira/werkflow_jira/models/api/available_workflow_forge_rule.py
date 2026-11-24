from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AvailableWorkflowForgeRule(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    ruleKey: StrictStr | None = None
    ruleType: StrictStr | None = None
