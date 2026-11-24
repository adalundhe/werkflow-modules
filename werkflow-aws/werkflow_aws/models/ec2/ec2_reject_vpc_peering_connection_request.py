from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2RejectVpcPeeringConnectionRequest(BaseModel):
    VpcPeeringConnectionId: StrictStr
    DryRun: StrictBool | None = None
