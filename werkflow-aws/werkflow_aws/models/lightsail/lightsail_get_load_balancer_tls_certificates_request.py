from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetLoadBalancerTlsCertificatesRequest(BaseModel):
    loadBalancerName: StrictStr
