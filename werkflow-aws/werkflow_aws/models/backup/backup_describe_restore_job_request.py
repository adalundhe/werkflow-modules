from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeRestoreJobRequest(BaseModel):
    RestoreJobId: StrictStr
