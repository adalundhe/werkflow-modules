from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_production_variant_managed_instance_scaling_scale_in_policy_model import SageMakerProductionVariantManagedInstanceScalingScaleInPolicyModel


class SageMakerProductionVariantManagedInstanceScalingModel(BaseModel):
    Status: StrictStr | None = None
    MinInstanceCount: StrictInt | None = None
    MaxInstanceCount: StrictInt | None = None
    ScaleInPolicy: SageMakerProductionVariantManagedInstanceScalingScaleInPolicyModel | None = None
