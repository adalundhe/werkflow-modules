from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AttachClassicLinkVpcRequest(BaseModel):
    InstanceId: StrictStr
    VpcId: StrictStr
    Groups: list[StrictStr]
    DryRun: StrictBool | None = None
