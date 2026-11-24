from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetRecoveryPointIndexDetailsRequest(BaseModel):
    BackupVaultName: StrictStr
    RecoveryPointArn: StrictStr
