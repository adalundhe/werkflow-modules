from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteNetworkInterfaceRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    DryRun: StrictBool | None = None
