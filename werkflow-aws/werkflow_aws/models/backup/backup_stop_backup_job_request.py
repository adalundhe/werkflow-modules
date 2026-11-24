from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupStopBackupJobRequest(BaseModel):
    BackupJobId: StrictStr
