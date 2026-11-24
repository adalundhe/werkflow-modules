from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_component_availability_zone_balance import SageMakerInferenceComponentAvailabilityZoneBalance


class SageMakerInferenceComponentSchedulingConfig(BaseModel):
    PlacementStrategy: StrictStr | None = None
    AvailabilityZoneBalance: SageMakerInferenceComponentAvailabilityZoneBalance | None = None
