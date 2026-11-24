from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZonePhysicalConnectionRequirements(BaseModel):
    subnetId: StrictStr | None = None
    subnetIdList: list[StrictStr] | None = None
    securityGroupIdList: list[StrictStr] | None = None
    availabilityZone: StrictStr | None = None
