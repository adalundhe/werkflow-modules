from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpcRequest(BaseModel):
    VpcId: StrictStr
    DryRun: StrictBool | None = None
