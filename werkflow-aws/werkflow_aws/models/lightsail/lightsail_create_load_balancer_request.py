from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateLoadBalancerRequest(BaseModel):
    loadBalancerName: StrictStr
    instancePort: StrictInt
    healthCheckPath: StrictStr | None = None
    certificateName: StrictStr | None = None
    certificateDomainName: StrictStr | None = None
    certificateAlternativeNames: list[StrictStr] | None = None
    tags: list[LightsailTag] | None = None
    ipAddressType: Literal['dualstack', 'ipv4', 'ipv6'] | None = None
    tlsPolicyName: StrictStr | None = None
