from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DeleteNetworkAclEntryRequest(BaseModel):
    NetworkAclId: StrictStr
    RuleNumber: StrictInt
    Egress: StrictBool
    DryRun: StrictBool | None = None
