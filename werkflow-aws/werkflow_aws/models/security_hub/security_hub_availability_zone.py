from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAvailabilityZone(BaseModel):
    ZoneName: StrictStr | None = None
    SubnetId: StrictStr | None = None
