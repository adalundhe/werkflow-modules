from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsWafRuleGroupRulesActionDetails(BaseModel):
    Type: StrictStr | None = None
