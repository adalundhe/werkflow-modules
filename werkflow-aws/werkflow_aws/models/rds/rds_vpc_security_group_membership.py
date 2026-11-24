from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSVpcSecurityGroupMembership(BaseModel):
    VpcSecurityGroupId: StrictStr | None = None
    Status: StrictStr | None = None
