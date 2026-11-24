from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeRecoveryPointRequest(BaseModel):
    BackupVaultName: StrictStr
    RecoveryPointArn: StrictStr
    BackupVaultAccountId: StrictStr | None = None
