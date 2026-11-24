from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume_model import RDSAdditionalStorageVolumeModel
from .rds_processor_feature_model import RDSProcessorFeatureModel
from .rds_tag_model import RDSTagModel


class RDSDBSnapshotModel(BaseModel):
    DBSnapshotIdentifier: StrictStr | None = None
    DBInstanceIdentifier: StrictStr | None = None
    SnapshotCreateTime: datetime.datetime | StrictStr | None = None
    Engine: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    Status: StrictStr | None = None
    Port: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    VpcId: StrictStr | None = None
    InstanceCreateTime: datetime.datetime | StrictStr | None = None
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
    StorageEncryptionType: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    DBSnapshotArn: StrictStr | None = None
    Timezone: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    ProcessorFeatures: list[RDSProcessorFeatureModel] | None = None
    DbiResourceId: StrictStr | None = None
    TagList: list[RDSTagModel] | None = None
    SnapshotTarget: StrictStr | None = None
    OriginalSnapshotCreateTime: datetime.datetime | StrictStr | None = None
    SnapshotDatabaseTime: datetime.datetime | StrictStr | None = None
    DBSystemId: StrictStr | None = None
    MultiTenant: StrictBool | None = None
    DedicatedLogVolume: StrictBool | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolumeModel] | None = None
    SnapshotAvailabilityZone: StrictStr | None = None
    FullSnapshotSizeInBytes: StrictInt | None = None
