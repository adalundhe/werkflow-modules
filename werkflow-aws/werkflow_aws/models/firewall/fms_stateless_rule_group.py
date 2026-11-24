from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FMSStatelessRuleGroup(BaseModel):
    RuleGroupName: StrictStr | None = None
    ResourceId: StrictStr | None = None
    Priority: StrictInt | None = None
