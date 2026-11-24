from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EC2LaunchTemplatePlacementRequest(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Affinity: StrictStr | None = None
    GroupName: StrictStr | None = None
    HostId: StrictStr | None = None
    Tenancy: Literal['default', 'dedicated', 'host'] | None = None
    SpreadDomain: StrictStr | None = None
    HostResourceGroupArn: StrictStr | None = None
    PartitionNumber: StrictInt | None = None
    GroupId: StrictStr | None = None
