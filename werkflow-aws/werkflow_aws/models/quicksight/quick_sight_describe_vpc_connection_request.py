from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeVPCConnectionRequest(BaseModel):
    AwsAccountId: StrictStr
    VPCConnectionId: StrictStr
