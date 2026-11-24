from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_hsm_backup import CloudHSMBackup


class CloudHSMModifyBackupAttributesResponse(BaseModel):
    Backup: CloudHSMBackup | None = None
    ResponseMetadata: dict[str, Any] | None = None
