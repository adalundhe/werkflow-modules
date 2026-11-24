from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_file_system import FSxFileSystem


class FSxUpdateFileSystemResponse(BaseModel):
    FileSystem: FSxFileSystem | None = None
    ResponseMetadata: dict[str, Any] | None = None
