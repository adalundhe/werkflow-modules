from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_load_balancer import LightsailLoadBalancer


class LightsailGetLoadBalancersResponse(BaseModel):
    loadBalancers: list[LightsailLoadBalancer] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
