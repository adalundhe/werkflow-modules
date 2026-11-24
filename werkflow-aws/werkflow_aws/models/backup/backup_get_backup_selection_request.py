from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetBackupSelectionRequest(BaseModel):
    BackupPlanId: StrictStr
    SelectionId: StrictStr
