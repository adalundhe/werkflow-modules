from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSFirewallSubnetIsOutOfScopeViolation(BaseModel):
    FirewallSubnetId: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetAvailabilityZone: StrictStr | None = None
    SubnetAvailabilityZoneId: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
