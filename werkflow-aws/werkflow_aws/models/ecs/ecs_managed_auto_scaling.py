from __future__ import annotations
from pydantic import BaseModel
from .ecs_managed_application_auto_scaling_policy import ECSManagedApplicationAutoScalingPolicy
from .ecs_managed_scalable_target import ECSManagedScalableTarget


class ECSManagedAutoScaling(BaseModel):
    scalableTarget: ECSManagedScalableTarget | None = None
    applicationAutoScalingPolicies: list[ECSManagedApplicationAutoScalingPolicy] | None = None
