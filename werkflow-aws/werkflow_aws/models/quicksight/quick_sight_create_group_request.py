from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCreateGroupRequest(BaseModel):
    GroupName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
    Description: StrictStr | None = None
