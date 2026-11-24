from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .efs_backup_policy import EFSBackupPolicy


class EFSPutBackupPolicyResponse(BaseModel):
    BackupPolicy: EFSBackupPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
