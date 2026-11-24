from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetRestoreTestingInferredMetadataRequest(BaseModel):
    BackupVaultName: StrictStr
    RecoveryPointArn: StrictStr
    BackupVaultAccountId: StrictStr | None = None
