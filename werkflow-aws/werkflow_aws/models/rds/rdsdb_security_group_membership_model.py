from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBSecurityGroupMembershipModel(BaseModel):
    DBSecurityGroupName: StrictStr | None = None
    Status: StrictStr | None = None
