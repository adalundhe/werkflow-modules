from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeUserRequest(BaseModel):
    UserName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
