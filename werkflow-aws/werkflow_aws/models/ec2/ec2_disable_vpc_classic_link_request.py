from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisableVpcClassicLinkRequest(BaseModel):
    VpcId: StrictStr
    DryRun: StrictBool | None = None
