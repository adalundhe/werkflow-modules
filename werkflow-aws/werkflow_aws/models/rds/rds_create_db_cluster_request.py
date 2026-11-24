from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_cluster_scalability_type import RDSClusterScalabilityType
from .rds_database_insights_mode import RDSDatabaseInsightsMode
from .rds_master_user_authentication_type import RDSMasterUserAuthenticationType
from .rds_rds_custom_cluster_configuration import RDSRdsCustomClusterConfiguration
from .rds_scaling_configuration import RDSScalingConfiguration
from .rds_serverless_v2_scaling_configuration import RDSServerlessV2ScalingConfiguration
from .rds_tag import RDSTag
from .rds_tag_specification import RDSTagSpecification
from .rdsdb_cluster_associated_role import RDSDBClusterAssociatedRole


class RDSCreateDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    Engine: StrictStr
    AvailabilityZones: list[StrictStr] | None = None
    BackupRetentionPeriod: StrictInt | None = None
    CharacterSetName: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    DBClusterParameterGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    DBSubnetGroupName: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    Port: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
    OptionGroupName: StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    ReplicationSourceIdentifier: StrictStr | None = None
    Tags: list[RDSTag] | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    PreSignedUrl: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    BacktrackWindow: StrictInt | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    EngineMode: StrictStr | None = None
    ScalingConfiguration: RDSScalingConfiguration | None = None
    RdsCustomClusterConfiguration: RDSRdsCustomClusterConfiguration | None = None
    DBClusterInstanceClass: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    StorageType: StrictStr | None = None
    Iops: StrictInt | None = None
    PubliclyAccessible: StrictBool | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    DeletionProtection: StrictBool | None = None
    GlobalClusterIdentifier: StrictStr | None = None
    EnableHttpEndpoint: StrictBool | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    Domain: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    EnableGlobalWriteForwarding: StrictBool | None = None
    NetworkType: StrictStr | None = None
    ServerlessV2ScalingConfiguration: RDSServerlessV2ScalingConfiguration | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    DatabaseInsightsMode: RDSDatabaseInsightsMode | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    EnableLimitlessDatabase: StrictBool | None = None
    ClusterScalabilityType: RDSClusterScalabilityType | None = None
    DBSystemId: StrictStr | None = None
    ManageMasterUserPassword: StrictBool | None = None
    EnableLocalWriteForwarding: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    EngineLifecycleSupport: StrictStr | None = None
    TagSpecifications: list[RDSTagSpecification] | None = None
    MasterUserAuthenticationType: RDSMasterUserAuthenticationType | None = None
    EnableVPCNetworking: StrictBool | None = None
    WithExpressConfiguration: StrictBool | None = None
    EnableInternetAccessGateway: StrictBool | None = None
    AssociatedRoles: list[RDSDBClusterAssociatedRole] | None = None
    SourceRegion: StrictStr | None = None
