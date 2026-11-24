from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .directory_service_directory_connect_settings import DirectoryServiceDirectoryConnectSettings
from .directory_service_tag import DirectoryServiceTag


class DirectoryServiceConnectDirectoryRequest(BaseModel):
    Name: StrictStr
    Password: StrictStr
    Size: Literal['Small', 'Large']
    ConnectSettings: DirectoryServiceDirectoryConnectSettings
    ShortName: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[DirectoryServiceTag] | None = None
    NetworkType: Literal['Dual-stack', 'IPv4', 'IPv6'] | None = None
