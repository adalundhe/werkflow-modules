from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListNamespacesRequest(BaseModel):
    AwsAccountId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
