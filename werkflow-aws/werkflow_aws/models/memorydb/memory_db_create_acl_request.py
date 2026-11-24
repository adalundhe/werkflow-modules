from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_tag import MemoryDBTag


class MemoryDBCreateACLRequest(BaseModel):
    ACLName: StrictStr
    UserNames: list[StrictStr] | None = None
    Tags: list[MemoryDBTag] | None = None
