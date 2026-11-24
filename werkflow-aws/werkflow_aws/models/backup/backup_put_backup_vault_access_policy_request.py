from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupPutBackupVaultAccessPolicyRequest(BaseModel):
    BackupVaultName: StrictStr
    Policy: StrictStr | None = None
