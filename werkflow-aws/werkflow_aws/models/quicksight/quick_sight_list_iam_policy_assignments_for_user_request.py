from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListIAMPolicyAssignmentsForUserRequest(BaseModel):
    AwsAccountId: StrictStr
    UserName: StrictStr
    Namespace: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
