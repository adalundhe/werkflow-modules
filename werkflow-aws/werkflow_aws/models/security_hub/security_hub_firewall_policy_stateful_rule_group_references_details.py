from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubFirewallPolicyStatefulRuleGroupReferencesDetails(BaseModel):
    ResourceArn: StrictStr | None = None
