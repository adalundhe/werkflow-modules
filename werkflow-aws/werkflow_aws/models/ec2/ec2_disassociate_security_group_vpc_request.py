from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisassociateSecurityGroupVpcRequest(BaseModel):
    GroupId: StrictStr
    VpcId: StrictStr
    DryRun: StrictBool | None = None
