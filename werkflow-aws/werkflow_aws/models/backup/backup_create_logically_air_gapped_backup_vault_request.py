from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupCreateLogicallyAirGappedBackupVaultRequest(BaseModel):
    BackupVaultName: StrictStr
    MinRetentionDays: StrictInt
    MaxRetentionDays: StrictInt
    BackupVaultTags: dict[StrictStr, StrictStr] | None = None
    CreatorRequestId: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
