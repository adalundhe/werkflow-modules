from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_file_cache import FSxFileCache


class FSxUpdateFileCacheResponse(BaseModel):
    FileCache: FSxFileCache | None = None
    ResponseMetadata: dict[str, Any] | None = None
