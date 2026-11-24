from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_managed_instance_scaling_status import SageMakerManagedInstanceScalingStatus
from .sage_maker_production_variant_managed_instance_scaling_scale_in_policy import SageMakerProductionVariantManagedInstanceScalingScaleInPolicy


class SageMakerProductionVariantManagedInstanceScaling(BaseModel):
    Status: SageMakerManagedInstanceScalingStatus | None = None
    MinInstanceCount: StrictInt | None = None
    MaxInstanceCount: StrictInt | None = None
    ScaleInPolicy: SageMakerProductionVariantManagedInstanceScalingScaleInPolicy | None = None
