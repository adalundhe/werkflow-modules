from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2IpamAddressHistoryRecord(BaseModel):
    ResourceOwnerId: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceCidr: StrictStr | None = None
    ResourceName: StrictStr | None = None
    ResourceComplianceStatus: StrictStr | None = None
    ResourceOverlapStatus: StrictStr | None = None
    VpcId: StrictStr | None = None
    SampledStartTime: datetime.datetime | StrictStr | None = None
    SampledEndTime: datetime.datetime | StrictStr | None = None
