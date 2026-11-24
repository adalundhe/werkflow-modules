from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .directory_service_shared_directory import DirectoryServiceSharedDirectory


class DirectoryServiceAcceptSharedDirectoryResponse(BaseModel):
    SharedDirectory: DirectoryServiceSharedDirectory | None = None
    ResponseMetadata: dict[str, Any] | None = None
