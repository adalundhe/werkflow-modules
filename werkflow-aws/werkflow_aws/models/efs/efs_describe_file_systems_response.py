from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .efs_file_system_description import EFSFileSystemDescription


class EFSDescribeFileSystemsResponse(BaseModel):
    Marker: StrictStr | None = None
    FileSystems: list[EFSFileSystemDescription] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
