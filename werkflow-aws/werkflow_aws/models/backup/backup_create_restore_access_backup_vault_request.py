from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupCreateRestoreAccessBackupVaultRequest(BaseModel):
    SourceBackupVaultArn: StrictStr
    BackupVaultName: StrictStr | None = None
    BackupVaultTags: dict[StrictStr, StrictStr] | None = None
    CreatorRequestId: StrictStr | None = None
    RequesterComment: StrictStr | None = None
