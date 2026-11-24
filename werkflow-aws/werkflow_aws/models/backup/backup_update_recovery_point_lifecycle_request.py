from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_lifecycle import BackupLifecycle


class BackupUpdateRecoveryPointLifecycleRequest(BaseModel):
    BackupVaultName: StrictStr
    RecoveryPointArn: StrictStr
    Lifecycle: BackupLifecycle | None = None
