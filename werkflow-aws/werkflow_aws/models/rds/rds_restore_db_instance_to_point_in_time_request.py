from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume_model import RDSAdditionalStorageVolumeModel
from .rds_processor_feature_model import RDSProcessorFeatureModel
from .rds_tag_model import RDSTagModel
from .rds_tag_specification_model import RDSTagSpecificationModel


class RDSRestoreDBInstanceToPointInTimeRequest(BaseModel):
    TargetDBInstanceIdentifier: StrictStr
    SourceDBInstanceIdentifier: StrictStr | None = None
    RestoreTime: datetime.datetime | StrictStr | None = None
    UseLatestRestorableTime: StrictBool | None = None
    DBInstanceClass: StrictStr | None = None
    Port: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    DBSubnetGroupName: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    PubliclyAccessible: StrictBool | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    LicenseModel: StrictStr | None = None
    DBName: StrictStr | None = None
    Engine: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    OptionGroupName: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    Tags: list[RDSTagModel] | None = None
    StorageType: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    TdeCredentialPassword: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    Domain: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    DomainFqdn: StrictStr | None = None
    DomainOu: StrictStr | None = None
    DomainAuthSecretArn: StrictStr | None = None
    DomainDnsIps: list[StrictStr] | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    ProcessorFeatures: list[RDSProcessorFeatureModel] | None = None
    UseDefaultProcessorFeatures: StrictBool | None = None
    DBParameterGroupName: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    SourceDbiResourceId: StrictStr | None = None
    MaxAllocatedStorage: StrictInt | None = None
    EnableCustomerOwnedIp: StrictBool | None = None
    NetworkType: StrictStr | None = None
    SourceDBInstanceAutomatedBackupsArn: StrictStr | None = None
    BackupTarget: StrictStr | None = None
    CustomIamInstanceProfile: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
    DedicatedLogVolume: StrictBool | None = None
    CACertificateIdentifier: StrictStr | None = None
    EngineLifecycleSupport: StrictStr | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolumeModel] | None = None
    TagSpecifications: list[RDSTagSpecificationModel] | None = None
    ManageMasterUserPassword: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
