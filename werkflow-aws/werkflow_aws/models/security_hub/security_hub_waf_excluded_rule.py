from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubWafExcludedRule(BaseModel):
    RuleId: StrictStr | None = None
