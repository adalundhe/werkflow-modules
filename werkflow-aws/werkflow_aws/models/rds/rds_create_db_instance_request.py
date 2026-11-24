from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume import RDSAdditionalStorageVolume
from .rds_database_insights_mode import RDSDatabaseInsightsMode
from .rds_master_user_authentication_type import RDSMasterUserAuthenticationType
from .rds_processor_feature import RDSProcessorFeature
from .rds_tag import RDSTag
from .rds_tag_specification import RDSTagSpecification


class RDSCreateDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    DBInstanceClass: StrictStr
    Engine: StrictStr
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
    CharacterSetName: StrictStr | None = None
    NcharCharacterSetName: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    Tags: list[RDSTag] | None = None
    DBClusterIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    TdeCredentialPassword: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    Domain: StrictStr | None = None
    DomainFqdn: StrictStr | None = None
    DomainOu: StrictStr | None = None
    DomainAuthSecretArn: StrictStr | None = None
    DomainDnsIps: list[StrictStr] | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    PromotionTier: StrictInt | None = None
    Timezone: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    DatabaseInsightsMode: RDSDatabaseInsightsMode | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    ProcessorFeatures: list[RDSProcessorFeature] | None = None
    DeletionProtection: StrictBool | None = None
    MaxAllocatedStorage: StrictInt | None = None
    EnableCustomerOwnedIp: StrictBool | None = None
    NetworkType: StrictStr | None = None
    BackupTarget: StrictStr | None = None
    CustomIamInstanceProfile: StrictStr | None = None
    DBSystemId: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    ManageMasterUserPassword: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
    MultiTenant: StrictBool | None = None
    DedicatedLogVolume: StrictBool | None = None
    EngineLifecycleSupport: StrictStr | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolume] | None = None
    TagSpecifications: list[RDSTagSpecification] | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
    MasterUserAuthenticationType: RDSMasterUserAuthenticationType | None = None
