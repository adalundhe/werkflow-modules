from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_tag import MemoryDBTag


class MemoryDBCreateParameterGroupRequest(BaseModel):
    ParameterGroupName: StrictStr
    Family: StrictStr
    Description: StrictStr | None = None
    Tags: list[MemoryDBTag] | None = None
