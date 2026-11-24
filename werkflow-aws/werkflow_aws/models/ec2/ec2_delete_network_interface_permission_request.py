from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteNetworkInterfacePermissionRequest(BaseModel):
    NetworkInterfacePermissionId: StrictStr
    Force: StrictBool | None = None
    DryRun: StrictBool | None = None
