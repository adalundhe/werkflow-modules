from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2PlacementModel(BaseModel):
    AvailabilityZoneId: StrictStr | None = None
    Affinity: StrictStr | None = None
    GroupName: StrictStr | None = None
    PartitionNumber: StrictInt | None = None
    HostId: StrictStr | None = None
    Tenancy: StrictStr | None = None
    SpreadDomain: StrictStr | None = None
    HostResourceGroupArn: StrictStr | None = None
    GroupId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
