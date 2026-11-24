from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume_model import RDSAdditionalStorageVolumeModel
from .rds_processor_feature_model import RDSProcessorFeatureModel
from .rds_tag_model import RDSTagModel
from .rds_tag_specification_model import RDSTagSpecificationModel


class RDSRestoreDBInstanceFromS3Request(BaseModel):
    DBInstanceIdentifier: StrictStr
    DBInstanceClass: StrictStr
    Engine: StrictStr
    SourceEngine: StrictStr
    SourceEngineVersion: StrictStr
    S3BucketName: StrictStr
    S3IngestionRoleArn: StrictStr
    DBName: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
    DBSecurityGroups: list[StrictStr] | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    AvailabilityZone: StrictStr | None = None
    DBSubnetGroupName: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    DBParameterGroupName: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    Port: StrictInt | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    OptionGroupName: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    Tags: list[RDSTagModel] | None = None
    StorageType: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    S3Prefix: StrictStr | None = None
    DatabaseInsightsMode: Literal['standard', 'advanced'] | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    ProcessorFeatures: list[RDSProcessorFeatureModel] | None = None
    UseDefaultProcessorFeatures: StrictBool | None = None
    DeletionProtection: StrictBool | None = None
    MaxAllocatedStorage: StrictInt | None = None
    NetworkType: StrictStr | None = None
    ManageMasterUserPassword: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
    DedicatedLogVolume: StrictBool | None = None
    CACertificateIdentifier: StrictStr | None = None
    EngineLifecycleSupport: StrictStr | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolumeModel] | None = None
    TagSpecifications: list[RDSTagSpecificationModel] | None = None
