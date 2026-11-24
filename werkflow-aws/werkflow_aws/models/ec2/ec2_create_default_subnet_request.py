from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CreateDefaultSubnetRequest(BaseModel):
    AvailabilityZone: StrictStr | None = None
    DryRun: StrictBool | None = None
    Ipv6Native: StrictBool | None = None
    AvailabilityZoneId: StrictStr | None = None
