from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SpotPlacement(BaseModel):
    AvailabilityZone: StrictStr | None = None
    GroupName: StrictStr | None = None
    Tenancy: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
