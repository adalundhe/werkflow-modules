from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_lifecycle import BackupLifecycle


class BackupCopyAction(BaseModel):
    Lifecycle: BackupLifecycle | None = None
    DestinationBackupVaultArn: StrictStr | None = None
