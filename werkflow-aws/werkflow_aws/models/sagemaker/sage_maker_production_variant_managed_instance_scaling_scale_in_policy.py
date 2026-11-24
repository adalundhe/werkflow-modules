from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_managed_instance_scaling_scale_in_strategy import SageMakerManagedInstanceScalingScaleInStrategy


class SageMakerProductionVariantManagedInstanceScalingScaleInPolicy(BaseModel):
    Strategy: SageMakerManagedInstanceScalingScaleInStrategy | None = None
    MaximumStepSize: StrictInt | None = None
    CooldownInMinutes: StrictInt | None = None
