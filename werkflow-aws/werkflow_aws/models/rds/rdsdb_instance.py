from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_activity_stream_mode import RDSActivityStreamMode
from .rds_activity_stream_policy_status import RDSActivityStreamPolicyStatus
from .rds_activity_stream_status import RDSActivityStreamStatus
from .rds_additional_storage_volume_output import RDSAdditionalStorageVolumeOutput
from .rds_automation_mode import RDSAutomationMode
from .rds_certificate_details import RDSCertificateDetails
from .rds_database_insights_mode import RDSDatabaseInsightsMode
from .rds_domain_membership import RDSDomainMembership
from .rds_endpoint import RDSEndpoint
from .rds_master_user_secret import RDSMasterUserSecret
from .rds_option_group_membership import RDSOptionGroupMembership
from .rds_pending_modified_values import RDSPendingModifiedValues
from .rds_primary_endpoint import RDSPrimaryEndpoint
from .rds_processor_feature import RDSProcessorFeature
from .rds_replica_mode import RDSReplicaMode
from .rds_storage_encryption_type import RDSStorageEncryptionType
from .rds_tag import RDSTag
from .rds_upgrade_rollout_order import RDSUpgradeRolloutOrder
from .rds_vpc_security_group_membership import RDSVpcSecurityGroupMembership
from .rdsdb_instance_automated_backups_replication import RDSDBInstanceAutomatedBackupsReplication
from .rdsdb_instance_role import RDSDBInstanceRole
from .rdsdb_instance_status_info import RDSDBInstanceStatusInfo
from .rdsdb_parameter_group_status import RDSDBParameterGroupStatus
from .rdsdb_security_group_membership import RDSDBSecurityGroupMembership
from .rdsdb_subnet_group import RDSDBSubnetGroup


class RDSDBInstance(BaseModel):
    DBInstanceIdentifier: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    Engine: StrictStr | None = None
    DBInstanceStatus: StrictStr | None = None
    MasterUsername: StrictStr | None = None
    DBName: StrictStr | None = None
    Endpoint: RDSEndpoint | None = None
    PrimaryEndpoint: RDSPrimaryEndpoint | None = None
    AllocatedStorage: StrictInt | None = None
    InstanceCreateTime: datetime.datetime | None = None
    PreferredBackupWindow: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    DBSecurityGroups: list[RDSDBSecurityGroupMembership] | None = None
    VpcSecurityGroups: list[RDSVpcSecurityGroupMembership] | None = None
    DBParameterGroups: list[RDSDBParameterGroupStatus] | None = None
    AvailabilityZone: StrictStr | None = None
    DBSubnetGroup: RDSDBSubnetGroup | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    UpgradeRolloutOrder: RDSUpgradeRolloutOrder | None = None
    PendingModifiedValues: RDSPendingModifiedValues | None = None
    LatestRestorableTime: datetime.datetime | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    ReadReplicaSourceDBInstanceIdentifier: StrictStr | None = None
    ReadReplicaDBInstanceIdentifiers: list[StrictStr] | None = None
    ReadReplicaDBClusterIdentifiers: list[StrictStr] | None = None
    ReplicaMode: RDSReplicaMode | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    OptionGroupMemberships: list[RDSOptionGroupMembership] | None = None
    CharacterSetName: StrictStr | None = None
    NcharCharacterSetName: StrictStr | None = None
    SecondaryAvailabilityZone: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    StatusInfos: list[RDSDBInstanceStatusInfo] | None = None
    StorageType: StrictStr | None = None
    StorageEncryptionType: RDSStorageEncryptionType | None = None
    TdeCredentialArn: StrictStr | None = None
    DbInstancePort: StrictInt | None = None
    DBClusterIdentifier: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    DomainMemberships: list[RDSDomainMembership] | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    EnhancedMonitoringResourceArn: StrictStr | None = None
    MonitoringRoleArn: StrictStr | None = None
    PromotionTier: StrictInt | None = None
    DBInstanceArn: StrictStr | None = None
    Timezone: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    DatabaseInsightsMode: RDSDatabaseInsightsMode | None = None
    PerformanceInsightsEnabled: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    EnabledCloudwatchLogsExports: list[StrictStr] | None = None
    ProcessorFeatures: list[RDSProcessorFeature] | None = None
    DeletionProtection: StrictBool | None = None
    AssociatedRoles: list[RDSDBInstanceRole] | None = None
    ListenerEndpoint: RDSEndpoint | None = None
    MaxAllocatedStorage: StrictInt | None = None
    TagList: list[RDSTag] | None = None
    AutomationMode: RDSAutomationMode | None = None
    ResumeFullAutomationModeTime: datetime.datetime | None = None
    CustomerOwnedIpEnabled: StrictBool | None = None
    NetworkType: StrictStr | None = None
    ActivityStreamStatus: RDSActivityStreamStatus | None = None
    ActivityStreamKmsKeyId: StrictStr | None = None
    ActivityStreamKinesisStreamName: StrictStr | None = None
    ActivityStreamMode: RDSActivityStreamMode | None = None
    ActivityStreamEngineNativeAuditFieldsIncluded: StrictBool | None = None
    AwsBackupRecoveryPointArn: StrictStr | None = None
    DBInstanceAutomatedBackupsReplications: list[RDSDBInstanceAutomatedBackupsReplication] | None = None
    BackupTarget: StrictStr | None = None
    AutomaticRestartTime: datetime.datetime | None = None
    CustomIamInstanceProfile: StrictStr | None = None
    ActivityStreamPolicyStatus: RDSActivityStreamPolicyStatus | None = None
    CertificateDetails: RDSCertificateDetails | None = None
    DBSystemId: StrictStr | None = None
    MasterUserSecret: RDSMasterUserSecret | None = None
    ReadReplicaSourceDBClusterIdentifier: StrictStr | None = None
    PercentProgress: StrictStr | None = None
    MultiTenant: StrictBool | None = None
    DedicatedLogVolume: StrictBool | None = None
    IsStorageConfigUpgradeAvailable: StrictBool | None = None
    EngineLifecycleSupport: StrictStr | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolumeOutput] | None = None
    StorageVolumeStatus: StrictStr | None = None
    StorageOperationStatus: StrictStr | None = None
    StorageOperationPercentProgress: StrictInt | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
    VPCNetworkingEnabled: StrictBool | None = None
