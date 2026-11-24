from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteBackupSelectionRequest(BaseModel):
    BackupPlanId: StrictStr
    SelectionId: StrictStr
