from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume import RDSAdditionalStorageVolume
from .rds_processor_feature import RDSProcessorFeature
from .rds_storage_encryption_type import RDSStorageEncryptionType
from .rds_tag import RDSTag


class RDSDBSnapshot(BaseModel):
    DBSnapshotIdentifier: StrictStr | None = None
    DBInstanceIdentifier: StrictStr | None = None
    SnapshotCreateTime: datetime.datetime | None = None
    Engine: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    Status: StrictStr | None = None
    Port: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    VpcId: StrictStr | None = None
    InstanceCreateTime: datetime.datetime | None = None
    MasterUsername: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    OptionGroupName: StrictStr | None = None
    PercentProgress: StrictInt | None = None
    SourceRegion: StrictStr | None = None
    SourceDBSnapshotIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    Encrypted: StrictBool | None = None
    StorageEncryptionType: RDSStorageEncryptionType | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    DBSnapshotArn: StrictStr | None = None
    Timezone: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    ProcessorFeatures: list[RDSProcessorFeature] | None = None
    DbiResourceId: StrictStr | None = None
    TagList: list[RDSTag] | None = None
    SnapshotTarget: StrictStr | None = None
    OriginalSnapshotCreateTime: datetime.datetime | None = None
    SnapshotDatabaseTime: datetime.datetime | None = None
    DBSystemId: StrictStr | None = None
    MultiTenant: StrictBool | None = None
    DedicatedLogVolume: StrictBool | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolume] | None = None
    SnapshotAvailabilityZone: StrictStr | None = None
    FullSnapshotSizeInBytes: StrictInt | None = None
