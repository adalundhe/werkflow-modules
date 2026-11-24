from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListProtectedResourcesByBackupVaultRequest(BaseModel):
    BackupVaultName: StrictStr
    BackupVaultAccountId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
