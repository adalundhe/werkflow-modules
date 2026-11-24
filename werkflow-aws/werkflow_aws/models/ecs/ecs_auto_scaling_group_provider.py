from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_managed_scaling import ECSManagedScaling


class ECSAutoScalingGroupProvider(BaseModel):
    autoScalingGroupArn: StrictStr | None = None
    managedScaling: ECSManagedScaling | None = None
    managedTerminationProtection: StrictStr | None = None
    managedDraining: StrictStr | None = None
