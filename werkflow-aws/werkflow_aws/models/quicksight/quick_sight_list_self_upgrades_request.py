from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListSelfUpgradesRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
