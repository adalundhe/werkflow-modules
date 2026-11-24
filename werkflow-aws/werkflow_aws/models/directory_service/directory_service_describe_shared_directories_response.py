from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_shared_directory import DirectoryServiceSharedDirectory


class DirectoryServiceDescribeSharedDirectoriesResponse(BaseModel):
    SharedDirectories: list[DirectoryServiceSharedDirectory] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
