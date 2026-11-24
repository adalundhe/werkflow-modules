from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailLoadBalancerTlsCertificateSummary(BaseModel):
    name: StrictStr | None = None
    isAttached: StrictBool | None = None
