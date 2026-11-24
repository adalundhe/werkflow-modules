from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Placement(BaseModel):
    AvailabilityZone: StrictStr | None = None
    GroupName: StrictStr | None = None
    Tenancy: StrictStr | None = None
    HostId: StrictStr | None = None
