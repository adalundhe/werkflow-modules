from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_load_balancer import ELBv2LoadBalancer


class ELBv2CreateLoadBalancerResponse(BaseModel):
    LoadBalancers: list[ELBv2LoadBalancer] | None = None
    ResponseMetadata: dict[str, Any] | None = None
