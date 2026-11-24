from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .backup_latest_revoke_request import BackupLatestRevokeRequest


class BackupRestoreAccessBackupVaultListMember(BaseModel):
    RestoreAccessBackupVaultArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    ApprovalDate: datetime.datetime | StrictStr | None = None
    VaultState: StrictStr | None = None
    LatestRevokeRequest: BackupLatestRevokeRequest | None = None
