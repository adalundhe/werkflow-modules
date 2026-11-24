from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AcceptVpcPeeringConnectionRequest(BaseModel):
    VpcPeeringConnectionId: StrictStr
    DryRun: StrictBool | None = None
