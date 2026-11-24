from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteUserRequest(BaseModel):
    UserName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
