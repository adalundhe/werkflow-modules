from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSAvailableCapacityPerAvailabilityZone(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailableCapacity: StrictInt | None = None
