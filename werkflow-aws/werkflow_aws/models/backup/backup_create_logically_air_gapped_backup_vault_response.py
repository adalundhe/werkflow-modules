from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupCreateLogicallyAirGappedBackupVaultResponse(BaseModel):
    BackupVaultName: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    VaultState: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
