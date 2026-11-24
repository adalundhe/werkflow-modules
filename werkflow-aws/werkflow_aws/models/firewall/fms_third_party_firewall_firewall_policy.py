from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSThirdPartyFirewallFirewallPolicy(BaseModel):
    FirewallPolicyId: StrictStr | None = None
    FirewallPolicyName: StrictStr | None = None
