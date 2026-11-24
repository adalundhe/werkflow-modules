from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2IpamRoutingPolicyRegistration(BaseModel):
    Cidr: StrictStr | None = None
    Asns: list[StrictStr] | None = None
    PermitMoreSpecificAnnouncements: StrictBool | None = None
    MaxLength: StrictInt | None = None
    Description: StrictStr | None = None
    LatestDeltaId: StrictStr | None = None
    State: StrictStr | None = None
