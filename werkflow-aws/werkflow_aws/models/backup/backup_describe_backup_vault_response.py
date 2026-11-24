from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .backup_latest_mpa_approval_team_update import BackupLatestMpaApprovalTeamUpdate


class BackupDescribeBackupVaultResponse(BaseModel):
    BackupVaultName: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
    VaultType: StrictStr | None = None
    VaultState: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    CreatorRequestId: StrictStr | None = None
    NumberOfRecoveryPoints: StrictInt | None = None
    Locked: StrictBool | None = None
    MinRetentionDays: StrictInt | None = None
    MaxRetentionDays: StrictInt | None = None
    LockDate: datetime.datetime | StrictStr | None = None
    SourceBackupVaultArn: StrictStr | None = None
    MpaApprovalTeamArn: StrictStr | None = None
    MpaSessionArn: StrictStr | None = None
    LatestMpaApprovalTeamUpdate: BackupLatestMpaApprovalTeamUpdate | None = None
    EncryptionKeyType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
