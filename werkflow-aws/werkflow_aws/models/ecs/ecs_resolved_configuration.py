from __future__ import annotations
from pydantic import BaseModel
from .ecs_service_revision_load_balancer import ECSServiceRevisionLoadBalancer
from .ecs_service_revision_vpc_lattice_configuration import ECSServiceRevisionVpcLatticeConfiguration


class ECSResolvedConfiguration(BaseModel):
    loadBalancers: list[ECSServiceRevisionLoadBalancer] | None = None
    vpcLatticeConfigurations: list[ECSServiceRevisionVpcLatticeConfiguration] | None = None
