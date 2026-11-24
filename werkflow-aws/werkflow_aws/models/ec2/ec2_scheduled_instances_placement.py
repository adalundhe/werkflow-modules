from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ScheduledInstancesPlacement(BaseModel):
    AvailabilityZone: StrictStr | None = None
    GroupName: StrictStr | None = None
