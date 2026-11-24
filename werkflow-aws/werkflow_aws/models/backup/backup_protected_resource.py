from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupProtectedResource(BaseModel):
    ResourceArn: StrictStr | None = None
    ResourceType: StrictStr | None = None
    LastBackupTime: datetime.datetime | StrictStr | None = None
    ResourceName: StrictStr | None = None
    LastBackupVaultArn: StrictStr | None = None
    LastRecoveryPointArn: StrictStr | None = None
