from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListFolderMembersRequest(BaseModel):
    AwsAccountId: StrictStr
    FolderId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
