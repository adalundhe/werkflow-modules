from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_managed_certificate import ECSManagedCertificate
from .ecs_managed_listener import ECSManagedListener
from .ecs_managed_listener_rule import ECSManagedListenerRule
from .ecs_managed_load_balancer import ECSManagedLoadBalancer
from .ecs_managed_security_group import ECSManagedSecurityGroup
from .ecs_managed_target_group import ECSManagedTargetGroup


class ECSManagedIngressPath(BaseModel):
    accessType: StrictStr | None = None
    endpoint: StrictStr | None = None
    loadBalancer: ECSManagedLoadBalancer | None = None
    loadBalancerSecurityGroups: list[ECSManagedSecurityGroup] | None = None
    certificate: ECSManagedCertificate | None = None
    listener: ECSManagedListener | None = None
    rule: ECSManagedListenerRule | None = None
    targetGroups: list[ECSManagedTargetGroup] | None = None
