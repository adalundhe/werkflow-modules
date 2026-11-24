from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateAddressRequest(BaseModel):
    AllocationId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    PublicIp: StrictStr | None = None
    DryRun: StrictBool | None = None
    NetworkInterfaceId: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    AllowReassociation: StrictBool | None = None
