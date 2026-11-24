from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerCapacityReservationResourceUsage(BaseModel):
    ResourceType: StrictStr | None = None
    InUseInstanceCount: StrictInt | None = None
