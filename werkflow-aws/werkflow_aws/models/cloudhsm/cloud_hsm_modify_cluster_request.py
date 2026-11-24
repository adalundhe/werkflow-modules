from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_hsm_backup_retention_policy import CloudHSMBackupRetentionPolicy


class CloudHSMModifyClusterRequest(BaseModel):
    ClusterId: StrictStr
    HsmType: StrictStr | None = None
    BackupRetentionPolicy: CloudHSMBackupRetentionPolicy | None = None
