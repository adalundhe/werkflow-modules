from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .backup_lifecycle import BackupLifecycle


class BackupStartBackupJobRequest(BaseModel):
    BackupVaultName: StrictStr
    ResourceArn: StrictStr
    IamRoleArn: StrictStr
    LogicallyAirGappedBackupVaultArn: StrictStr | None = None
    IdempotencyToken: StrictStr | None = None
    StartWindowMinutes: StrictInt | None = None
    CompleteWindowMinutes: StrictInt | None = None
    Lifecycle: BackupLifecycle | None = None
    RecoveryPointTags: dict[StrictStr, StrictStr] | None = None
    BackupOptions: dict[StrictStr, StrictStr] | None = None
    Index: Literal['ENABLED', 'DISABLED'] | None = None
