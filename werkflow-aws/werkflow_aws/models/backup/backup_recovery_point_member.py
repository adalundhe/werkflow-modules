from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupRecoveryPointMember(BaseModel):
    RecoveryPointArn: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    ResourceType: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
