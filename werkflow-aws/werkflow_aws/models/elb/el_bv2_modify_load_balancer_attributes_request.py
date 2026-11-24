from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_load_balancer_attribute import ELBv2LoadBalancerAttribute


class ELBv2ModifyLoadBalancerAttributesRequest(BaseModel):
    LoadBalancerArn: StrictStr
    Attributes: list[ELBv2LoadBalancerAttribute]
