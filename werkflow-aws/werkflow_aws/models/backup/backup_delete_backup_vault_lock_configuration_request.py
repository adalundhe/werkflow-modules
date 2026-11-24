from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteBackupVaultLockConfigurationRequest(BaseModel):
    BackupVaultName: StrictStr
