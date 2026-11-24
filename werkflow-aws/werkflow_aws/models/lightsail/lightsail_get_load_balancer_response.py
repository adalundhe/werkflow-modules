from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_load_balancer import LightsailLoadBalancer


class LightsailGetLoadBalancerResponse(BaseModel):
    loadBalancer: LightsailLoadBalancer | None = None
    ResponseMetadata: dict[str, Any] | None = None
