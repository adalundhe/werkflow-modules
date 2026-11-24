from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceIpRouteInfo(BaseModel):
    DirectoryId: StrictStr | None = None
    CidrIp: StrictStr | None = None
    CidrIpv6: StrictStr | None = None
    IpRouteStatusMsg: StrictStr | None = None
    AddedDateTime: datetime.datetime | StrictStr | None = None
    IpRouteStatusReason: StrictStr | None = None
    Description: StrictStr | None = None
