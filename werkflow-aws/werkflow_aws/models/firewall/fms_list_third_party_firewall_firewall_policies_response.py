from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_third_party_firewall_firewall_policy import FMSThirdPartyFirewallFirewallPolicy


class FMSListThirdPartyFirewallFirewallPoliciesResponse(BaseModel):
    ThirdPartyFirewallFirewallPolicies: list[FMSThirdPartyFirewallFirewallPolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
