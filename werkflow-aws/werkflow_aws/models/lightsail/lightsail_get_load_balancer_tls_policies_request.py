from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetLoadBalancerTlsPoliciesRequest(BaseModel):
    pageToken: StrictStr | None = None
