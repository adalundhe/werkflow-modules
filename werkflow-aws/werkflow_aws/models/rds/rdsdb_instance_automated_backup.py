from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume_model import RDSAdditionalStorageVolumeModel
from .rdsdb_instance_automated_backups_replication_model import RDSDBInstanceAutomatedBackupsReplicationModel
from .rds_restore_window import RDSRestoreWindow
from .rds_tag_model import RDSTagModel


class RDSDBInstanceAutomatedBackup(BaseModel):
    DBInstanceArn: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
    Region: StrictStr | None = None
    DBInstanceIdentifier: StrictStr | None = None
    RestoreWindow: RDSRestoreWindow | None = None
    AllocatedStorage: StrictInt | None = None
    Status: StrictStr | None = None
    Port: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    VpcId: StrictStr | None = None
    InstanceCreateTime: datetime.datetime | StrictStr | None = None
    MasterUsername: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    OptionGroupName: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    Encrypted: StrictBool | None = None
    StorageEncryptionType: StrictStr | None = None
    StorageType: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Timezone: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    DBInstanceAutomatedBackupsArn: StrictStr | None = None
    DBInstanceAutomatedBackupsReplications: list[RDSDBInstanceAutomatedBackupsReplicationModel] | None = None
    BackupTarget: StrictStr | None = None
    MultiTenant: StrictBool | None = None
    AwsBackupRecoveryPointArn: StrictStr | None = None
    TagList: list[RDSTagModel] | None = None
    DedicatedLogVolume: StrictBool | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolumeModel] | None = None
