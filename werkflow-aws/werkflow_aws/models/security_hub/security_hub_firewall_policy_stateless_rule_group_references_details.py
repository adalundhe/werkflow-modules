from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubFirewallPolicyStatelessRuleGroupReferencesDetails(BaseModel):
    Priority: StrictInt | None = None
    ResourceArn: StrictStr | None = None
