from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CapacityReservationStatus(BaseModel):
    CapacityReservationId: StrictStr | None = None
    TotalCapacity: StrictInt | None = None
    TotalAvailableCapacity: StrictInt | None = None
    TotalUnavailableCapacity: StrictInt | None = None
