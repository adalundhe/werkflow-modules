from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteBackupPlanRequest(BaseModel):
    BackupPlanId: StrictStr
