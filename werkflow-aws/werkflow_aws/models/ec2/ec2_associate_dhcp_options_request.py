from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateDhcpOptionsRequest(BaseModel):
    DhcpOptionsId: StrictStr
    VpcId: StrictStr
    DryRun: StrictBool | None = None
