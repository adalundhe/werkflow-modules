from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsWafRegionalRuleGroupRulesActionDetails(BaseModel):
    Type: StrictStr | None = None
