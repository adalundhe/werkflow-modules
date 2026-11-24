from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class BackupListBackupVaultsRequest(BaseModel):
    ByVaultType: Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT', 'RESTORE_ACCESS_BACKUP_VAULT'] | None = None
    ByShared: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
