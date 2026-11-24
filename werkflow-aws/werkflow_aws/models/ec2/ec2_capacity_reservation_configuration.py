from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CapacityReservationConfiguration(BaseModel):
    InstanceCount: StrictInt | None = None
    ReservationState: StrictStr | None = None
