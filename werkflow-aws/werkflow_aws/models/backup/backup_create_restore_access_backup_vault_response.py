from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupCreateRestoreAccessBackupVaultResponse(BaseModel):
    RestoreAccessBackupVaultArn: StrictStr | None = None
    VaultState: StrictStr | None = None
    RestoreAccessBackupVaultName: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
