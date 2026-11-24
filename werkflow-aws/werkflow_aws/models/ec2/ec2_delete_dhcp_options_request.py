from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteDhcpOptionsRequest(BaseModel):
    DhcpOptionsId: StrictStr
    DryRun: StrictBool | None = None
