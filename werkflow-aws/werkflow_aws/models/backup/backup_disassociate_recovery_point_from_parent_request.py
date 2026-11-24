from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDisassociateRecoveryPointFromParentRequest(BaseModel):
    BackupVaultName: StrictStr
    RecoveryPointArn: StrictStr
