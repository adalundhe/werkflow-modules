from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteNetworkAclRequest(BaseModel):
    NetworkAclId: StrictStr
    DryRun: StrictBool | None = None
