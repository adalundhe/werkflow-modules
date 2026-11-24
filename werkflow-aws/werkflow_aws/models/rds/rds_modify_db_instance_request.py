from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_automation_mode import RDSAutomationMode
from .rds_cloudwatch_logs_export_configuration import RDSCloudwatchLogsExportConfiguration
from .rds_database_insights_mode import RDSDatabaseInsightsMode
from .rds_master_user_authentication_type import RDSMasterUserAuthenticationType
from .rds_modify_additional_storage_volume import RDSModifyAdditionalStorageVolume
from .rds_processor_feature import RDSProcessorFeature
from .rds_replica_mode import RDSReplicaMode
from .rds_tag_specification import RDSTagSpecification


class RDSModifyDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    AllocatedStorage: StrictInt | None = None
    DBInstanceClass: StrictStr | None = None
    DBSubnetGroupName: StrictStr | None = None
    DBSecurityGroups: list[StrictStr] | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    ApplyImmediately: StrictBool | None = None
    MasterUserPassword: StrictStr | None = None
    DBParameterGroupName: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AllowMajorVersionUpgrade: StrictBool | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    OptionGroupName: StrictStr | None = None
    NewDBInstanceIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    TdeCredentialPassword: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    Domain: StrictStr | None = None
    DomainFqdn: StrictStr | None = None
    DomainOu: StrictStr | None = None
    DomainAuthSecretArn: StrictStr | None = None
    DomainDnsIps: list[StrictStr] | None = None
    DisableDomain: StrictBool | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    DBPortNumber: StrictInt | None = None
    PubliclyAccessible: StrictBool | None = None
    MonitoringRoleArn: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    PromotionTier: StrictInt | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    DatabaseInsightsMode: RDSDatabaseInsightsMode | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    CloudwatchLogsExportConfiguration: RDSCloudwatchLogsExportConfiguration | None = None
    ProcessorFeatures: list[RDSProcessorFeature] | None = None
    UseDefaultProcessorFeatures: StrictBool | None = None
    DeletionProtection: StrictBool | None = None
    MaxAllocatedStorage: StrictInt | None = None
    CertificateRotationRestart: StrictBool | None = None
    ReplicaMode: RDSReplicaMode | None = None
    AutomationMode: RDSAutomationMode | None = None
    ResumeFullAutomationModeMinutes: StrictInt | None = None
    EnableCustomerOwnedIp: StrictBool | None = None
    NetworkType: StrictStr | None = None
    AwsBackupRecoveryPointArn: StrictStr | None = None
    ManageMasterUserPassword: StrictBool | None = None
    RotateMasterUserPassword: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
    MultiTenant: StrictBool | None = None
    DedicatedLogVolume: StrictBool | None = None
    Engine: StrictStr | None = None
    AdditionalStorageVolumes: list[RDSModifyAdditionalStorageVolume] | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
    TagSpecifications: list[RDSTagSpecification] | None = None
    MasterUserAuthenticationType: RDSMasterUserAuthenticationType | None = None
    EngineLifecycleSupport: StrictStr | None = None
