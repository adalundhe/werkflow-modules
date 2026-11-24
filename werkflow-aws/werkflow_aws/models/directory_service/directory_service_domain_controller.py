from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceDomainController(BaseModel):
    DirectoryId: StrictStr | None = None
    DomainControllerId: StrictStr | None = None
    DnsIpAddr: StrictStr | None = None
    DnsIpv6Addr: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    LaunchTime: datetime.datetime | StrictStr | None = None
    StatusLastUpdatedDateTime: datetime.datetime | StrictStr | None = None
