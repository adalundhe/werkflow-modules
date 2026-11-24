from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteDBSecurityGroupRequest(BaseModel):
    DBSecurityGroupName: StrictStr
