from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ecs_managed_scaling import ECSManagedScaling


class ECSAutoScalingGroupProviderUpdate(BaseModel):
    managedScaling: ECSManagedScaling | None = None
    managedTerminationProtection: Literal['ENABLED', 'DISABLED'] | None = None
    managedDraining: Literal['ENABLED', 'DISABLED'] | None = None
