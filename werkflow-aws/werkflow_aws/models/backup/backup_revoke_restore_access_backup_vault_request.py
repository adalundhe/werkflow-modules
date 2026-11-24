from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupRevokeRestoreAccessBackupVaultRequest(BaseModel):
    BackupVaultName: StrictStr
    RestoreAccessBackupVaultArn: StrictStr
    RequesterComment: StrictStr | None = None
