from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .directory_service_directory_size_update_settings import DirectoryServiceDirectorySizeUpdateSettings
from .directory_service_network_update_settings import DirectoryServiceNetworkUpdateSettings
from .directory_service_os_update_settings import DirectoryServiceOSUpdateSettings


class DirectoryServiceUpdateDirectorySetupRequest(BaseModel):
    DirectoryId: StrictStr
    UpdateType: Literal['OS', 'NETWORK', 'SIZE']
    OSUpdateSettings: DirectoryServiceOSUpdateSettings | None = None
    DirectorySizeUpdateSettings: DirectoryServiceDirectorySizeUpdateSettings | None = None
    NetworkUpdateSettings: DirectoryServiceNetworkUpdateSettings | None = None
    CreateSnapshotBeforeUpdate: StrictBool | None = None
