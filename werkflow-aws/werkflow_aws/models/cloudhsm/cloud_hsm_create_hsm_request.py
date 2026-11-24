from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMCreateHsmRequest(BaseModel):
    ClusterId: StrictStr
    AvailabilityZone: StrictStr
    IpAddress: StrictStr | None = None
