from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListGroupMembershipsRequest(BaseModel):
    GroupName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
