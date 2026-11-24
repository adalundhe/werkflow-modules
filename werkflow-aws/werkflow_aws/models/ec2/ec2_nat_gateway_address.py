from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2NatGatewayAddress(BaseModel):
    AllocationId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    PrivateIp: StrictStr | None = None
    PublicIp: StrictStr | None = None
    AssociationId: StrictStr | None = None
    IsPrimary: StrictBool | None = None
    FailureMessage: StrictStr | None = None
    Status: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
