from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsNetworkFirewallFirewallSubnetMappingsDetails(BaseModel):
    SubnetId: StrictStr | None = None
