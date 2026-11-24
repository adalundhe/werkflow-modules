from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_ip_route_info import DirectoryServiceIpRouteInfo


class DirectoryServiceListIpRoutesResponse(BaseModel):
    IpRoutesInfo: list[DirectoryServiceIpRouteInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
