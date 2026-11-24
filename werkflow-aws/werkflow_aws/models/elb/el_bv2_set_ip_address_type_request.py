from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ELBv2SetIpAddressTypeRequest(BaseModel):
    LoadBalancerArn: StrictStr
    IpAddressType: Literal['ipv4', 'dualstack', 'dualstack-without-public-ipv4']
