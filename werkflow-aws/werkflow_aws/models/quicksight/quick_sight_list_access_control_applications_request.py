from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListAccessControlApplicationsRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
