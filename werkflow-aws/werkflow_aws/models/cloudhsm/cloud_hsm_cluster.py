from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_hsm_backup_retention_policy import CloudHSMBackupRetentionPolicy
from .cloud_hsm_certificates import CloudHSMCertificates
from .cloud_hsm_hsm import CloudHSMHsm
from .cloud_hsm_tag import CloudHSMTag


class CloudHSMCluster(BaseModel):
    BackupPolicy: StrictStr | None = None
    BackupRetentionPolicy: CloudHSMBackupRetentionPolicy | None = None
    ClusterId: StrictStr | None = None
    CreateTimestamp: datetime.datetime | StrictStr | None = None
    Hsms: list[CloudHSMHsm] | None = None
    HsmType: StrictStr | None = None
    HsmTypeRollbackExpiration: datetime.datetime | StrictStr | None = None
    PreCoPassword: StrictStr | None = None
    SecurityGroup: StrictStr | None = None
    SourceBackupId: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    SubnetMapping: dict[StrictStr, StrictStr] | None = None
    VpcId: StrictStr | None = None
    NetworkType: StrictStr | None = None
    Certificates: CloudHSMCertificates | None = None
    TagList: list[CloudHSMTag] | None = None
    Mode: StrictStr | None = None
