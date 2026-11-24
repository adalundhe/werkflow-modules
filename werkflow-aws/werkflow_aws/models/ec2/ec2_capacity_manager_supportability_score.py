from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CapacityManagerSupportabilityScore(BaseModel):
    InstanceType: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Score: StrictStr | None = None
