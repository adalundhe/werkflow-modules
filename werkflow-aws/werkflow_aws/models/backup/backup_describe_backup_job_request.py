from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeBackupJobRequest(BaseModel):
    BackupJobId: StrictStr
