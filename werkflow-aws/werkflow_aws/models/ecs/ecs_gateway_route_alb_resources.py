from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_gateway_route_load_balancer_security_group import ECSGatewayRouteLoadBalancerSecurityGroup


class ECSGatewayRouteAlbResources(BaseModel):
    acmCertificateArn: StrictStr | None = None
    loadBalancerArn: StrictStr | None = None
    listenerArn: StrictStr | None = None
    listenerRuleArn: StrictStr | None = None
    testListenerRuleArns: list[StrictStr] | None = None
    loadBalancerSecurityGroups: list[ECSGatewayRouteLoadBalancerSecurityGroup] | None = None
    serviceSecurityGroupArn: StrictStr | None = None
