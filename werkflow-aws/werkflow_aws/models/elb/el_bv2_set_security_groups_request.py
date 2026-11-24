from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ELBv2SetSecurityGroupsRequest(BaseModel):
    LoadBalancerArn: StrictStr
    SecurityGroups: list[StrictStr]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: Literal['on', 'off'] | None = None
