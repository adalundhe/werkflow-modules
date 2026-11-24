from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_load_balancer_attribute import ELBv2LoadBalancerAttribute


class ELBv2ModifyLoadBalancerAttributesResponse(BaseModel):
    Attributes: list[ELBv2LoadBalancerAttribute] | None = None
    ResponseMetadata: dict[str, Any] | None = None
