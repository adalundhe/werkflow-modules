from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_availability_zone import DMSAvailabilityZone


class DMSSubnet(BaseModel):
    SubnetIdentifier: StrictStr | None = None
    SubnetAvailabilityZone: DMSAvailabilityZone | None = None
    SubnetStatus: StrictStr | None = None
