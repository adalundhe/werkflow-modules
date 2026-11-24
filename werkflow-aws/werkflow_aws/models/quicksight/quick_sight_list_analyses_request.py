from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListAnalysesRequest(BaseModel):
    AwsAccountId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
