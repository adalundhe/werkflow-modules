from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDBSecurityGroupMembership(BaseModel):
    DBSecurityGroupName: StrictStr | None = None
    Status: StrictStr | None = None
