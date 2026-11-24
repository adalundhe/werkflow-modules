from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupPutBackupVaultLockConfigurationRequest(BaseModel):
    BackupVaultName: StrictStr
    MinRetentionDays: StrictInt | None = None
    MaxRetentionDays: StrictInt | None = None
    ChangeableForDays: StrictInt | None = None
