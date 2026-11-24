from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpcPeeringConnectionRequest(BaseModel):
    VpcPeeringConnectionId: StrictStr
    DryRun: StrictBool | None = None
