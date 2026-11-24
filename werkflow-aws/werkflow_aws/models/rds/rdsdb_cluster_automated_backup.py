from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_restore_window import RDSRestoreWindow
from .rds_tag_model import RDSTagModel


class RDSDBClusterAutomatedBackup(BaseModel):
    Engine: StrictStr | None = None
    VpcId: StrictStr | None = None
    DBClusterAutomatedBackupsArn: StrictStr | None = None
    DBClusterIdentifier: StrictStr | None = None
    RestoreWindow: RDSRestoreWindow | None = None
    MasterUsername: StrictStr | None = None
    DbClusterResourceId: StrictStr | None = None
    Region: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    Status: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    ClusterCreateTime: datetime.datetime | StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    StorageEncryptionType: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    EngineVersion: StrictStr | None = None
    DBClusterArn: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    EngineMode: StrictStr | None = None
    AvailabilityZones: list[StrictStr] | None = None
    Port: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    StorageType: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    AwsBackupRecoveryPointArn: StrictStr | None = None
    TagList: list[RDSTagModel] | None = None
