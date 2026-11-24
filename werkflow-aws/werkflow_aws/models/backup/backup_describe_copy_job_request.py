from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeCopyJobRequest(BaseModel):
    CopyJobId: StrictStr
