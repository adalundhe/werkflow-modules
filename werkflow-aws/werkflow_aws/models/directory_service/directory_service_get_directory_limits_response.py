from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .directory_service_directory_limits import DirectoryServiceDirectoryLimits


class DirectoryServiceGetDirectoryLimitsResponse(BaseModel):
    DirectoryLimits: DirectoryServiceDirectoryLimits | None = None
    ResponseMetadata: dict[str, Any] | None = None
