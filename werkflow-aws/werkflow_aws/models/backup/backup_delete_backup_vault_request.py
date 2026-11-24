from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteBackupVaultRequest(BaseModel):
    BackupVaultName: StrictStr
