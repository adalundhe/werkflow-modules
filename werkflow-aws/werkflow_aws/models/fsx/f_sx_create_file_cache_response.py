from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_file_cache_creating import FSxFileCacheCreating


class FSxCreateFileCacheResponse(BaseModel):
    FileCache: FSxFileCacheCreating | None = None
    ResponseMetadata: dict[str, Any] | None = None
