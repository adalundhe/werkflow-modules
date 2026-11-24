from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListAppsRequest(BaseModel):
    AwsAccountId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
