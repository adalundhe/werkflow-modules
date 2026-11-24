from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeBackupVaultRequest(BaseModel):
    BackupVaultName: StrictStr
    BackupVaultAccountId: StrictStr | None = None
