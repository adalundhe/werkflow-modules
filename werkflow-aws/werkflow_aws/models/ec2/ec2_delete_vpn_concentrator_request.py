from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpnConcentratorRequest(BaseModel):
    VpnConcentratorId: StrictStr
    DryRun: StrictBool | None = None
