from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteVPCConnectionRequest(BaseModel):
    AwsAccountId: StrictStr
    VPCConnectionId: StrictStr
