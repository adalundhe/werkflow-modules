from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2IpamDiscoveredRoute(BaseModel):
    IpamResourceDiscoveryId: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    ResourceOwnerId: StrictStr | None = None
    Cidr: StrictStr | None = None
    Asn: StrictStr | None = None
    State: StrictStr | None = None
    AdvertisementType: StrictStr | None = None
    NetworkBorderGroup: StrictStr | None = None
    PoolId: StrictStr | None = None
    IpamPoolId: StrictStr | None = None
    SampleTime: datetime.datetime | StrictStr | None = None
