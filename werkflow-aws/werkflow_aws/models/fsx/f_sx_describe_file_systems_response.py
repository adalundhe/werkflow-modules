from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_file_system import FSxFileSystem


class FSxDescribeFileSystemsResponse(BaseModel):
    FileSystems: list[FSxFileSystem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
