from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AvailabilityZoneAddress(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    AllocationIds: list[StrictStr] | None = None
