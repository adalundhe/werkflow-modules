from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_tag import MemoryDBTag


class MemoryDBCreateSubnetGroupRequest(BaseModel):
    SubnetGroupName: StrictStr
    SubnetIds: list[StrictStr]
    Description: StrictStr | None = None
    Tags: list[MemoryDBTag] | None = None
