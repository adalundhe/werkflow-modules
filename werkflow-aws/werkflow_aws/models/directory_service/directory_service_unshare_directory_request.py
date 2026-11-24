from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_unshare_target import DirectoryServiceUnshareTarget


class DirectoryServiceUnshareDirectoryRequest(BaseModel):
    DirectoryId: StrictStr
    UnshareTarget: DirectoryServiceUnshareTarget
