from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupCreateBackupVaultRequest(BaseModel):
    BackupVaultName: StrictStr
    BackupVaultTags: dict[StrictStr, StrictStr] | None = None
    EncryptionKeyArn: StrictStr | None = None
    CreatorRequestId: StrictStr | None = None
