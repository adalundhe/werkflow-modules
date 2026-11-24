from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ScheduledInstancesPrivateIpAddressConfig(BaseModel):
    Primary: StrictBool | None = None
    PrivateIpAddress: StrictStr | None = None
