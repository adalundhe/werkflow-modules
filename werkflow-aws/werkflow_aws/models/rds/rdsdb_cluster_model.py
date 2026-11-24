from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_certificate_details_model import RDSCertificateDetailsModel
from .rds_cluster_pending_modified_values_model import RDSClusterPendingModifiedValuesModel
from .rdsdb_cluster_member_model import RDSDBClusterMemberModel
from .rdsdb_cluster_option_group_status_model import RDSDBClusterOptionGroupStatusModel
from .rdsdb_cluster_role_model import RDSDBClusterRoleModel
from .rdsdb_cluster_status_info_model import RDSDBClusterStatusInfoModel
from .rds_domain_membership_model import RDSDomainMembershipModel
from .rds_limitless_database_model import RDSLimitlessDatabaseModel
from .rds_master_user_secret_model import RDSMasterUserSecretModel
from .rds_scaling_configuration_info_model import RDSScalingConfigurationInfoModel
from .rds_serverless_v2_scaling_configuration_info_model import RDSServerlessV2ScalingConfigurationInfoModel
from .rds_tag_model import RDSTagModel
from .rds_vpc_security_group_membership_model import RDSVpcSecurityGroupMembershipModel
from .rds_custom_cluster_configuration import RdsCustomClusterConfiguration as _RdsCustomClusterConfigurationType


class RDSDBClusterModel(BaseModel):
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
    EarliestRestorableTime: datetime.datetime | StrictStr | None = None
    Endpoint: StrictStr | None = None
    ReaderEndpoint: StrictStr | None = None
    CustomEndpoints: list[StrictStr] | None = None
    MultiAZ: StrictBool | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    LatestRestorableTime: datetime.datetime | StrictStr | None = None
    Port: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    DBClusterOptionGroupMemberships: list[RDSDBClusterOptionGroupStatusModel] | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    UpgradeRolloutOrder: StrictStr | None = None
    ReplicationSourceIdentifier: StrictStr | None = None
    ReadReplicaIdentifiers: list[StrictStr] | None = None
    StatusInfos: list[RDSDBClusterStatusInfoModel] | None = None
    DBClusterMembers: list[RDSDBClusterMemberModel] | None = None
    VpcSecurityGroups: list[RDSVpcSecurityGroupMembershipModel] | None = None
    HostedZoneId: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    StorageEncryptionType: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    DbClusterResourceId: StrictStr | None = None
    DBClusterArn: StrictStr | None = None
    AssociatedRoles: list[RDSDBClusterRoleModel] | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    CloneGroupId: StrictStr | None = None
    ClusterCreateTime: datetime.datetime | StrictStr | None = None
    EarliestBacktrackTime: datetime.datetime | StrictStr | None = None
    BacktrackWindow: StrictInt | None = None
    BacktrackConsumedChangeRecords: StrictInt | None = None
    EnabledCloudwatchLogsExports: list[StrictStr] | None = None
    Capacity: StrictInt | None = None
    PendingModifiedValues: RDSClusterPendingModifiedValuesModel | None = None
    EngineMode: StrictStr | None = None
    ScalingConfigurationInfo: RDSScalingConfigurationInfoModel | None = None
    RdsCustomClusterConfiguration: _RdsCustomClusterConfigurationType | None = None
    DBClusterInstanceClass: StrictStr | None = None
    StorageType: StrictStr | None = None
    Iops: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    IOOptimizedNextAllowedModificationTime: datetime.datetime | StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    DeletionProtection: StrictBool | None = None
    HttpEndpointEnabled: StrictBool | None = None
    ActivityStreamMode: StrictStr | None = None
    ActivityStreamStatus: StrictStr | None = None
    ActivityStreamKmsKeyId: StrictStr | None = None
    ActivityStreamKinesisStreamName: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    CrossAccountClone: StrictBool | None = None
    DomainMemberships: list[RDSDomainMembershipModel] | None = None
    TagList: list[RDSTagModel] | None = None
    GlobalClusterIdentifier: StrictStr | None = None
    GlobalWriteForwardingStatus: StrictStr | None = None
    GlobalWriteForwardingRequested: StrictBool | None = None
    NetworkType: StrictStr | None = None
    AutomaticRestartTime: datetime.datetime | StrictStr | None = None
    ServerlessV2ScalingConfiguration: RDSServerlessV2ScalingConfigurationInfoModel | None = None
    ServerlessV2PlatformVersion: StrictStr | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    DatabaseInsightsMode: StrictStr | None = None
    PerformanceInsightsEnabled: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    DBSystemId: StrictStr | None = None
    MasterUserSecret: RDSMasterUserSecretModel | None = None
    LocalWriteForwardingStatus: StrictStr | None = None
    AwsBackupRecoveryPointArn: StrictStr | None = None
    LimitlessDatabase: RDSLimitlessDatabaseModel | None = None
    ClusterScalabilityType: StrictStr | None = None
    CertificateDetails: RDSCertificateDetailsModel | None = None
    EngineLifecycleSupport: StrictStr | None = None
    VPCNetworkingEnabled: StrictBool | None = None
    InternetAccessGatewayEnabled: StrictBool | None = None
