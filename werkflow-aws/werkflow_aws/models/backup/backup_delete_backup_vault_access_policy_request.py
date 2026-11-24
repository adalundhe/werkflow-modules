from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteBackupVaultAccessPolicyRequest(BaseModel):
    BackupVaultName: StrictStr
