from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_load_balancer_tls_policy import LightsailLoadBalancerTlsPolicy


class LightsailGetLoadBalancerTlsPoliciesResponse(BaseModel):
    tlsPolicies: list[LightsailLoadBalancerTlsPolicy] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
