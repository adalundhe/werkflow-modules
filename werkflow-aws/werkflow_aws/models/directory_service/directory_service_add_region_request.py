from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_directory_vpc_settings import DirectoryServiceDirectoryVpcSettings


class DirectoryServiceAddRegionRequest(BaseModel):
    DirectoryId: StrictStr
    RegionName: StrictStr
    VPCSettings: DirectoryServiceDirectoryVpcSettings
