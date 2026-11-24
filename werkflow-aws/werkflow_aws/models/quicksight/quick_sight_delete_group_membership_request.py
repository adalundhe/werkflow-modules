from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteGroupMembershipRequest(BaseModel):
    MemberName: StrictStr
    GroupName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
