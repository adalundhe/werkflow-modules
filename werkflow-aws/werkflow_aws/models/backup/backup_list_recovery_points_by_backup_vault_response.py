from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_recovery_point_by_backup_vault import BackupRecoveryPointByBackupVault


class BackupListRecoveryPointsByBackupVaultResponse(BaseModel):
    NextToken: StrictStr | None = None
    RecoveryPoints: list[BackupRecoveryPointByBackupVault] | None = None
    ResponseMetadata: dict[str, Any] | None = None
