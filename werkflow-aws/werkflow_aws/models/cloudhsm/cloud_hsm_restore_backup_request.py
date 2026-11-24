from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMRestoreBackupRequest(BaseModel):
    BackupId: StrictStr
