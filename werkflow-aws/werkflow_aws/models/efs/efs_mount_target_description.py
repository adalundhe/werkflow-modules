from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSMountTargetDescription(BaseModel):
    OwnerId: StrictStr | None = None
    MountTargetId: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    LifeCycleState: StrictStr | None = None
    IpAddress: StrictStr | None = None
    Ipv6Address: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    AvailabilityZoneName: StrictStr | None = None
    VpcId: StrictStr | None = None
