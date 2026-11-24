from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_restore_access_backup_vault_list_member import BackupRestoreAccessBackupVaultListMember


class BackupListRestoreAccessBackupVaultsResponse(BaseModel):
    NextToken: StrictStr | None = None
    RestoreAccessBackupVaults: list[BackupRestoreAccessBackupVaultListMember] | None = None
    ResponseMetadata: dict[str, Any] | None = None
