from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteBackupVaultNotificationsRequest(BaseModel):
    BackupVaultName: StrictStr
