from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DetachClassicLinkVpcRequest(BaseModel):
    InstanceId: StrictStr
    VpcId: StrictStr
    DryRun: StrictBool | None = None
