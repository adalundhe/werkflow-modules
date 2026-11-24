from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateLoadBalancerTlsCertificateRequest(BaseModel):
    loadBalancerName: StrictStr
    certificateName: StrictStr
    certificateDomainName: StrictStr
    certificateAlternativeNames: list[StrictStr] | None = None
    tags: list[LightsailTag] | None = None
