from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_activity_stream_mode import RDSActivityStreamMode
from .rds_activity_stream_status import RDSActivityStreamStatus
from .rds_certificate_details import RDSCertificateDetails
from .rds_cluster_pending_modified_values import RDSClusterPendingModifiedValues
from .rds_cluster_scalability_type import RDSClusterScalabilityType
from .rds_database_insights_mode import RDSDatabaseInsightsMode
from .rds_domain_membership import RDSDomainMembership
from .rds_limitless_database import RDSLimitlessDatabase
from .rds_local_write_forwarding_status import RDSLocalWriteForwardingStatus
from .rds_master_user_secret import RDSMasterUserSecret
from .rds_rds_custom_cluster_configuration import RDSRdsCustomClusterConfiguration
from .rds_scaling_configuration_info import RDSScalingConfigurationInfo
from .rds_serverless_v2_scaling_configuration_info import RDSServerlessV2ScalingConfigurationInfo
from .rds_storage_encryption_type import RDSStorageEncryptionType
from .rds_tag import RDSTag
from .rds_upgrade_rollout_order import RDSUpgradeRolloutOrder
from .rds_vpc_security_group_membership import RDSVpcSecurityGroupMembership
from .rds_write_forwarding_status import RDSWriteForwardingStatus
from .rdsdb_cluster_member import RDSDBClusterMember
from .rdsdb_cluster_option_group_status import RDSDBClusterOptionGroupStatus
from .rdsdb_cluster_role import RDSDBClusterRole
from .rdsdb_cluster_status_info import RDSDBClusterStatusInfo


class RDSDBCluster(BaseModel):
    AllocatedStorage: StrictInt | None = None
    AvailabilityZones: list[StrictStr] | None = None
    BackupRetentionPeriod: StrictInt | None = None
    CharacterSetName: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    DBClusterIdentifier: StrictStr | None = None
    DBClusterParameterGroup: StrictStr | None = None
    DBSubnetGroup: StrictStr | None = None
    Status: StrictStr | None = None
    PercentProgress: StrictStr | None = None
    EarliestRestorableTime: datetime.datetime | None = None
    Endpoint: StrictStr | None = None
    ReaderEndpoint: StrictStr | None = None
    CustomEndpoints: list[StrictStr] | None = None
    MultiAZ: StrictBool | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    LatestRestorableTime: datetime.datetime | None = None
    Port: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    DBClusterOptionGroupMemberships: list[RDSDBClusterOptionGroupStatus] | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    UpgradeRolloutOrder: RDSUpgradeRolloutOrder | None = None
    ReplicationSourceIdentifier: StrictStr | None = None
    ReadReplicaIdentifiers: list[StrictStr] | None = None
    StatusInfos: list[RDSDBClusterStatusInfo] | None = None
    DBClusterMembers: list[RDSDBClusterMember] | None = None
    VpcSecurityGroups: list[RDSVpcSecurityGroupMembership] | None = None
    HostedZoneId: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    StorageEncryptionType: RDSStorageEncryptionType | None = None
    KmsKeyId: StrictStr | None = None
    DbClusterResourceId: StrictStr | None = None
    DBClusterArn: StrictStr | None = None
    AssociatedRoles: list[RDSDBClusterRole] | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    CloneGroupId: StrictStr | None = None
    ClusterCreateTime: datetime.datetime | None = None
    EarliestBacktrackTime: datetime.datetime | None = None
    BacktrackWindow: StrictInt | None = None
    BacktrackConsumedChangeRecords: StrictInt | None = None
    EnabledCloudwatchLogsExports: list[StrictStr] | None = None
    Capacity: StrictInt | None = None
    PendingModifiedValues: RDSClusterPendingModifiedValues | None = None
    EngineMode: StrictStr | None = None
    ScalingConfigurationInfo: RDSScalingConfigurationInfo | None = None
    RdsCustomClusterConfiguration: RDSRdsCustomClusterConfiguration | None = None
    DBClusterInstanceClass: StrictStr | None = None
    StorageType: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    IOOptimizedNextAllowedModificationTime: datetime.datetime | None = None
    PubliclyAccessible: StrictBool | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    DeletionProtection: StrictBool | None = None
    HttpEndpointEnabled: StrictBool | None = None
    ActivityStreamMode: RDSActivityStreamMode | None = None
    ActivityStreamStatus: RDSActivityStreamStatus | None = None
    ActivityStreamKmsKeyId: StrictStr | None = None
    ActivityStreamKinesisStreamName: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    CrossAccountClone: StrictBool | None = None
    DomainMemberships: list[RDSDomainMembership] | None = None
    TagList: list[RDSTag] | None = None
    GlobalClusterIdentifier: StrictStr | None = None
    GlobalWriteForwardingStatus: RDSWriteForwardingStatus | None = None
    GlobalWriteForwardingRequested: StrictBool | None = None
    NetworkType: StrictStr | None = None
    AutomaticRestartTime: datetime.datetime | None = None
    ServerlessV2ScalingConfiguration: RDSServerlessV2ScalingConfigurationInfo | None = None
    ServerlessV2PlatformVersion: StrictStr | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    DatabaseInsightsMode: RDSDatabaseInsightsMode | None = None
    PerformanceInsightsEnabled: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    DBSystemId: StrictStr | None = None
    MasterUserSecret: RDSMasterUserSecret | None = None
    LocalWriteForwardingStatus: RDSLocalWriteForwardingStatus | None = None
    AwsBackupRecoveryPointArn: StrictStr | None = None
    LimitlessDatabase: RDSLimitlessDatabase | None = None
    ClusterScalabilityType: RDSClusterScalabilityType | None = None
    CertificateDetails: RDSCertificateDetails | None = None
    EngineLifecycleSupport: StrictStr | None = None
    VPCNetworkingEnabled: StrictBool | None = None
    InternetAccessGatewayEnabled: StrictBool | None = None
