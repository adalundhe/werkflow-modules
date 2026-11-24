from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListFoldersForResourceRequest(BaseModel):
    AwsAccountId: StrictStr
    ResourceArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
