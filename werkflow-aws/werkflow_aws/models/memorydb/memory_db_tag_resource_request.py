from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_tag import MemoryDBTag


class MemoryDBTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[MemoryDBTag]
