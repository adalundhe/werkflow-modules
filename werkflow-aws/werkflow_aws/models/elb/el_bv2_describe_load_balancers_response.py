from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_load_balancer import ELBv2LoadBalancer


class ELBv2DescribeLoadBalancersResponse(BaseModel):
    LoadBalancers: list[ELBv2LoadBalancer] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
