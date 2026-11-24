from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAICapacityReservationConfig(BaseModel):
    CapacityReservationPreference: StrictStr | None = None
    MlReservationArns: list[StrictStr] | None = None
