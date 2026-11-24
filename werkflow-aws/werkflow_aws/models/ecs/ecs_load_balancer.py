from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_advanced_configuration import ECSAdvancedConfiguration


class ECSLoadBalancer(BaseModel):
    targetGroupArn: StrictStr | None = None
    loadBalancerName: StrictStr | None = None
    containerName: StrictStr | None = None
    containerPort: StrictInt | None = None
    advancedConfiguration: ECSAdvancedConfiguration | None = None
