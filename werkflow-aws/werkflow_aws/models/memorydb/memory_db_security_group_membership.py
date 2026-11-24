from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBSecurityGroupMembership(BaseModel):
    SecurityGroupId: StrictStr | None = None
    Status: StrictStr | None = None
