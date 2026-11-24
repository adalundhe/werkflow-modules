from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetBackupVaultAccessPolicyRequest(BaseModel):
    BackupVaultName: StrictStr
