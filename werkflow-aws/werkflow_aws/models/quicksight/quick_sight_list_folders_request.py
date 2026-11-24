from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListFoldersRequest(BaseModel):
    AwsAccountId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
