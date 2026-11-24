from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_desired_weight_and_capacity import SageMakerDesiredWeightAndCapacity


class SageMakerUpdateEndpointWeightsAndCapacitiesRequest(BaseModel):
    EndpointName: StrictStr
    DesiredWeightsAndCapacities: list[SageMakerDesiredWeightAndCapacity]
