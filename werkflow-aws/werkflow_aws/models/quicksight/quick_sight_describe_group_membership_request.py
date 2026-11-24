from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeGroupMembershipRequest(BaseModel):
    MemberName: StrictStr
    GroupName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
