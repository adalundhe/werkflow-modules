from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_additional_storage_volume_output_model import RDSAdditionalStorageVolumeOutputModel
from .rds_certificate_details_model import RDSCertificateDetailsModel
from .rdsdb_instance_automated_backups_replication_model import RDSDBInstanceAutomatedBackupsReplicationModel
from .rdsdb_instance_role_model import RDSDBInstanceRoleModel
from .rdsdb_instance_status_info_model import RDSDBInstanceStatusInfoModel
from .rdsdb_parameter_group_status_model import RDSDBParameterGroupStatusModel
from .rdsdb_security_group_membership_model import RDSDBSecurityGroupMembershipModel
from .rdsdb_subnet_group_model import RDSDBSubnetGroupModel
from .rds_domain_membership_model import RDSDomainMembershipModel
from .rds_endpoint_model import RDSEndpointModel
from .rds_master_user_secret_model import RDSMasterUserSecretModel
from .rds_option_group_membership_model import RDSOptionGroupMembershipModel
from .rds_pending_modified_values_model import RDSPendingModifiedValuesModel
from .rds_primary_endpoint_model import RDSPrimaryEndpointModel
from .rds_processor_feature_model import RDSProcessorFeatureModel
from .rds_tag_model import RDSTagModel
from .rds_vpc_security_group_membership_model import RDSVpcSecurityGroupMembershipModel


class RDSDBInstanceModel(BaseModel):
    DBInstanceIdentifier: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    Engine: StrictStr | None = None
    DBInstanceStatus: StrictStr | None = None
    MasterUsername: StrictStr | None = None
    DBName: StrictStr | None = None
    Endpoint: RDSEndpointModel | None = None
    PrimaryEndpoint: RDSPrimaryEndpointModel | None = None
    AllocatedStorage: StrictInt | None = None
    InstanceCreateTime: datetime.datetime | StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    DBSecurityGroups: list[RDSDBSecurityGroupMembershipModel] | None = None
    VpcSecurityGroups: list[RDSVpcSecurityGroupMembershipModel] | None = None
    DBParameterGroups: list[RDSDBParameterGroupStatusModel] | None = None
    AvailabilityZone: StrictStr | None = None
    DBSubnetGroup: RDSDBSubnetGroupModel | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    UpgradeRolloutOrder: StrictStr | None = None
    PendingModifiedValues: RDSPendingModifiedValuesModel | None = None
    LatestRestorableTime: datetime.datetime | StrictStr | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    ReadReplicaSourceDBInstanceIdentifier: StrictStr | None = None
    ReadReplicaDBInstanceIdentifiers: list[StrictStr] | None = None
    ReadReplicaDBClusterIdentifiers: list[StrictStr] | None = None
    ReplicaMode: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    OptionGroupMemberships: list[RDSOptionGroupMembershipModel] | None = None
    CharacterSetName: StrictStr | None = None
    NcharCharacterSetName: StrictStr | None = None
    SecondaryAvailabilityZone: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    StatusInfos: list[RDSDBInstanceStatusInfoModel] | None = None
    StorageType: StrictStr | None = None
    StorageEncryptionType: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    DbInstancePort: StrictInt | None = None
    DBClusterIdentifier: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    DomainMemberships: list[RDSDomainMembershipModel] | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    EnhancedMonitoringResourceArn: StrictStr | None = None
    MonitoringRoleArn: StrictStr | None = None
    PromotionTier: StrictInt | None = None
    DBInstanceArn: StrictStr | None = None
    Timezone: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    DatabaseInsightsMode: StrictStr | None = None
    PerformanceInsightsEnabled: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    EnabledCloudwatchLogsExports: list[StrictStr] | None = None
    ProcessorFeatures: list[RDSProcessorFeatureModel] | None = None
    DeletionProtection: StrictBool | None = None
    AssociatedRoles: list[RDSDBInstanceRoleModel] | None = None
    ListenerEndpoint: RDSEndpointModel | None = None
    MaxAllocatedStorage: StrictInt | None = None
    TagList: list[RDSTagModel] | None = None
    AutomationMode: StrictStr | None = None
    ResumeFullAutomationModeTime: datetime.datetime | StrictStr | None = None
    CustomerOwnedIpEnabled: StrictBool | None = None
    NetworkType: StrictStr | None = None
    ActivityStreamStatus: StrictStr | None = None
    ActivityStreamKmsKeyId: StrictStr | None = None
    ActivityStreamKinesisStreamName: StrictStr | None = None
    ActivityStreamMode: StrictStr | None = None
    ActivityStreamEngineNativeAuditFieldsIncluded: StrictBool | None = None
    AwsBackupRecoveryPointArn: StrictStr | None = None
    DBInstanceAutomatedBackupsReplications: list[RDSDBInstanceAutomatedBackupsReplicationModel] | None = None
    BackupTarget: StrictStr | None = None
    AutomaticRestartTime: datetime.datetime | StrictStr | None = None
    CustomIamInstanceProfile: StrictStr | None = None
    ActivityStreamPolicyStatus: StrictStr | None = None
    CertificateDetails: RDSCertificateDetailsModel | None = None
    DBSystemId: StrictStr | None = None
    MasterUserSecret: RDSMasterUserSecretModel | None = None
    ReadReplicaSourceDBClusterIdentifier: StrictStr | None = None
    PercentProgress: StrictStr | None = None
    MultiTenant: StrictBool | None = None
    DedicatedLogVolume: StrictBool | None = None
    IsStorageConfigUpgradeAvailable: StrictBool | None = None
    EngineLifecycleSupport: StrictStr | None = None
    AdditionalStorageVolumes: list[RDSAdditionalStorageVolumeOutputModel] | None = None
    StorageVolumeStatus: StrictStr | None = None
    StorageOperationStatus: StrictStr | None = None
    StorageOperationPercentProgress: StrictInt | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
    VPCNetworkingEnabled: StrictBool | None = None
