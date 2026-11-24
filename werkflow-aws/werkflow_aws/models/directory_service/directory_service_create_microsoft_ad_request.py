from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .directory_service_directory_vpc_settings import DirectoryServiceDirectoryVpcSettings
from .directory_service_tag import DirectoryServiceTag


class DirectoryServiceCreateMicrosoftADRequest(BaseModel):
    Name: StrictStr
    Password: StrictStr
    VpcSettings: DirectoryServiceDirectoryVpcSettings
    ShortName: StrictStr | None = None
    Description: StrictStr | None = None
    Edition: Literal['Enterprise', 'Standard', 'Hybrid'] | None = None
    Tags: list[DirectoryServiceTag] | None = None
    NetworkType: Literal['Dual-stack', 'IPv4', 'IPv6'] | None = None
