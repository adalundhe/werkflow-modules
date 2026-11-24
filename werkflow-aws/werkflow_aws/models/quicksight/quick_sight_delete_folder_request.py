from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteFolderRequest(BaseModel):
    AwsAccountId: StrictStr
    FolderId: StrictStr
