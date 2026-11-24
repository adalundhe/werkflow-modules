from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class BackupVaultListMember(BaseModel):
    BackupVaultName: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
    VaultType: StrictStr | None = None
    VaultState: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    CreatorRequestId: StrictStr | None = None
    NumberOfRecoveryPoints: StrictInt | None = None
    Locked: StrictBool | None = None
    MinRetentionDays: StrictInt | None = None
    MaxRetentionDays: StrictInt | None = None
    LockDate: datetime.datetime | StrictStr | None = None
    EncryptionKeyType: StrictStr | None = None
