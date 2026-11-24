from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateNatGatewayAddressRequest(BaseModel):
    NatGatewayId: StrictStr
    AllocationIds: list[StrictStr]
    PrivateIpAddresses: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
