from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeFolderRequest(BaseModel):
    AwsAccountId: StrictStr
    FolderId: StrictStr
