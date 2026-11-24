from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListActionConnectorsRequest(BaseModel):
    AwsAccountId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
