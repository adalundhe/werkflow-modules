from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_hsm_backup_retention_policy import CloudHSMBackupRetentionPolicy
from .cloud_hsm_tag import CloudHSMTag


class CloudHSMCreateClusterRequest(BaseModel):
    HsmType: StrictStr
    SubnetIds: list[StrictStr]
    BackupRetentionPolicy: CloudHSMBackupRetentionPolicy | None = None
    SourceBackupId: StrictStr | None = None
    NetworkType: Literal['IPV4', 'DUALSTACK'] | None = None
    TagList: list[CloudHSMTag] | None = None
    Mode: Literal['FIPS', 'NON_FIPS'] | None = None
