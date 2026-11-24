from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .directory_service_ip_route import DirectoryServiceIpRoute


class DirectoryServiceAddIpRoutesRequest(BaseModel):
    DirectoryId: StrictStr
    IpRoutes: list[DirectoryServiceIpRoute]
    UpdateSecurityGroupForDirectoryControllers: StrictBool | None = None
