from __future__ import annotations
from pydantic import BaseModel
from .ec2_classic_load_balancers_config import EC2ClassicLoadBalancersConfig
from .ec2_target_groups_config import EC2TargetGroupsConfig


class EC2LoadBalancersConfig(BaseModel):
    ClassicLoadBalancersConfig: EC2ClassicLoadBalancersConfig | None = None
    TargetGroupsConfig: EC2TargetGroupsConfig | None = None
