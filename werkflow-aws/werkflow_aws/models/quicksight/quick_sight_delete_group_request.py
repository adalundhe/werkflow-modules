from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteGroupRequest(BaseModel):
    GroupName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
