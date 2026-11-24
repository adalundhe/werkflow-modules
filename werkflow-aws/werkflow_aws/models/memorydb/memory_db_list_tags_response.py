from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .memory_db_tag import MemoryDBTag


class MemoryDBListTagsResponse(BaseModel):
    TagList: list[MemoryDBTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
