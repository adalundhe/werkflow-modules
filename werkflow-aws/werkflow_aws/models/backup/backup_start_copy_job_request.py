from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_lifecycle import BackupLifecycle


class BackupStartCopyJobRequest(BaseModel):
    RecoveryPointArn: StrictStr
    SourceBackupVaultName: StrictStr
    DestinationBackupVaultArn: StrictStr
    IamRoleArn: StrictStr
    IdempotencyToken: StrictStr | None = None
    Lifecycle: BackupLifecycle | None = None
