from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_directory_description import DirectoryServiceDirectoryDescription


class DirectoryServiceDescribeDirectoriesResponse(BaseModel):
    DirectoryDescriptions: list[DirectoryServiceDirectoryDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
