from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetBackupVaultNotificationsRequest(BaseModel):
    BackupVaultName: StrictStr
