from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .directory_service_directory_vpc_settings import DirectoryServiceDirectoryVpcSettings
from .directory_service_tag import DirectoryServiceTag


class DirectoryServiceCreateDirectoryRequest(BaseModel):
    Name: StrictStr
    Password: StrictStr
    Size: Literal['Small', 'Large']
    ShortName: StrictStr | None = None
    Description: StrictStr | None = None
    VpcSettings: DirectoryServiceDirectoryVpcSettings | None = None
    Tags: list[DirectoryServiceTag] | None = None
    NetworkType: Literal['Dual-stack', 'IPv4', 'IPv6'] | None = None
