from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .direct_connect_as_path_segment import DirectConnectAsPathSegment


class DirectConnectRoute(BaseModel):
    cidr: StrictStr | None = None
    routeDirection: StrictStr | None = None
    addressFamily: StrictStr | None = None
    asPath: list[DirectConnectAsPathSegment] | None = None
    communities: list[StrictStr] | None = None
    awsLogicalDeviceId: StrictStr | None = None
    routeInstalledAt: datetime.datetime | StrictStr | None = None
