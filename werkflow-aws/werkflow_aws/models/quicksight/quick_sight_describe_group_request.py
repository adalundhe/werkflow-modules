from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeGroupRequest(BaseModel):
    GroupName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
