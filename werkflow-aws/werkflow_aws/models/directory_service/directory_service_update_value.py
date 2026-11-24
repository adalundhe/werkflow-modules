from __future__ import annotations
from pydantic import BaseModel
from .directory_service_os_update_settings import DirectoryServiceOSUpdateSettings


class DirectoryServiceUpdateValue(BaseModel):
    OSUpdateSettings: DirectoryServiceOSUpdateSettings | None = None
