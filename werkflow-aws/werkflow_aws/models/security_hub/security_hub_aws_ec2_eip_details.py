from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2EipDetails(BaseModel):
    InstanceId: StrictStr | None = None
    PublicIp: StrictStr | None = None
    AllocationId: StrictStr | None = None
    AssociationId: StrictStr | None = None
    Domain: StrictStr | None = None
    PublicIpv4Pool: StrictStr | None = None
    NetworkBorderGroup: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    NetworkInterfaceOwnerId: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
