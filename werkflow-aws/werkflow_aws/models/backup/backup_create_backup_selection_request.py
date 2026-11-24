from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_selection import BackupSelection as _BackupSelectionType


class BackupCreateBackupSelectionRequest(BaseModel):
    BackupPlanId: StrictStr
    BackupSelection: _BackupSelectionType
    CreatorRequestId: StrictStr | None = None
