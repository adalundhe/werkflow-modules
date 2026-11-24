from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailDeleteLoadBalancerTlsCertificateRequest(BaseModel):
    loadBalancerName: StrictStr
    certificateName: StrictStr
    force: StrictBool | None = None
