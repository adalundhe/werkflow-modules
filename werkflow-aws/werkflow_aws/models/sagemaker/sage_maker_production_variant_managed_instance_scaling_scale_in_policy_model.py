from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerProductionVariantManagedInstanceScalingScaleInPolicyModel(BaseModel):
    Strategy: StrictStr | None = None
    MaximumStepSize: StrictInt | None = None
    CooldownInMinutes: StrictInt | None = None
