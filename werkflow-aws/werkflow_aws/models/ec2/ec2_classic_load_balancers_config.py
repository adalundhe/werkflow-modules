from __future__ import annotations
from pydantic import BaseModel
from .ec2_classic_load_balancer import EC2ClassicLoadBalancer


class EC2ClassicLoadBalancersConfig(BaseModel):
    ClassicLoadBalancers: list[EC2ClassicLoadBalancer] | None = None
