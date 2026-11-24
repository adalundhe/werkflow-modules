from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBDeleteSubnetGroupRequest(BaseModel):
    SubnetGroupName: StrictStr
