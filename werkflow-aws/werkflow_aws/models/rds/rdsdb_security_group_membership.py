from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBSecurityGroupMembership(BaseModel):
    DBSecurityGroupName: StrictStr | None = None
    Status: StrictStr | None = None
