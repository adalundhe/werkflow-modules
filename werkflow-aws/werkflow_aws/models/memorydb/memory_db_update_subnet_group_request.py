from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBUpdateSubnetGroupRequest(BaseModel):
    SubnetGroupName: StrictStr
    Description: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
