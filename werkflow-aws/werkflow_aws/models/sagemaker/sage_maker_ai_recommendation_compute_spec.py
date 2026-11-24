from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_capacity_reservation_config import SageMakerAICapacityReservationConfig


class SageMakerAIRecommendationComputeSpec(BaseModel):
    InstanceTypes: list[StrictStr] | None = None
    CapacityReservationConfig: SageMakerAICapacityReservationConfig | None = None
