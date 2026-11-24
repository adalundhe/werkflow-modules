from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2LaunchTemplatePlacement(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Affinity: StrictStr | None = None
    GroupName: StrictStr | None = None
    HostId: StrictStr | None = None
    Tenancy: StrictStr | None = None
    SpreadDomain: StrictStr | None = None
    HostResourceGroupArn: StrictStr | None = None
    PartitionNumber: StrictInt | None = None
    GroupId: StrictStr | None = None
