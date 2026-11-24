from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .efs_backup_policy import EFSBackupPolicy


class EFSPutBackupPolicyRequest(BaseModel):
    FileSystemId: StrictStr
    BackupPolicy: EFSBackupPolicy
