from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDescribeFolderPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    FolderId: StrictStr
    Namespace: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
