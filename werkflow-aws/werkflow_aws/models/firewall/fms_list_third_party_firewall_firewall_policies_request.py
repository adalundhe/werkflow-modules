from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class FMSListThirdPartyFirewallFirewallPoliciesRequest(BaseModel):
    ThirdPartyFirewall: Literal['PALO_ALTO_NETWORKS_CLOUD_NGFW', 'FORTIGATE_CLOUD_NATIVE_FIREWALL']
    MaxResults: StrictInt
    NextToken: StrictStr | None = None
