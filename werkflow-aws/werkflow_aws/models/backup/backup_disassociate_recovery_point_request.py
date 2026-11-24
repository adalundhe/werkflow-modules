from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDisassociateRecoveryPointRequest(BaseModel):
    BackupVaultName: StrictStr
    RecoveryPointArn: StrictStr
