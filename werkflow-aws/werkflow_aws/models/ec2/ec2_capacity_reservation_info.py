from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CapacityReservationInfo(BaseModel):
    InstanceType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Tenancy: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
