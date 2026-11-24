from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListRestoreAccessBackupVaultsRequest(BaseModel):
    BackupVaultName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
