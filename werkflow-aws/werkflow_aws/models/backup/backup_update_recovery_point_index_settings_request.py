from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BackupUpdateRecoveryPointIndexSettingsRequest(BaseModel):
    BackupVaultName: StrictStr
    RecoveryPointArn: StrictStr
    Index: Literal['ENABLED', 'DISABLED']
    IamRoleArn: StrictStr | None = None
