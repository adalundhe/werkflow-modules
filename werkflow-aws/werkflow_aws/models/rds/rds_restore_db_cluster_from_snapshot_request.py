from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rdsdb_cluster_associated_role_model import RDSDBClusterAssociatedRoleModel
from .rds_scaling_configuration_model import RDSScalingConfigurationModel
from .rds_serverless_v2_scaling_configuration_model import RDSServerlessV2ScalingConfigurationModel
from .rds_tag_model import RDSTagModel
from .rds_tag_specification_model import RDSTagSpecificationModel
from .rds_custom_cluster_configuration import RdsCustomClusterConfiguration as _RdsCustomClusterConfigurationType


class RDSRestoreDBClusterFromSnapshotRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    SnapshotIdentifier: StrictStr
    Engine: StrictStr
    AvailabilityZones: list[StrictStr] | None = None
    EngineVersion: StrictStr | None = None
    Port: StrictInt | None = None
    DBSubnetGroupName: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    OptionGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    Tags: list[RDSTagModel] | None = None
    KmsKeyId: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    BacktrackWindow: StrictInt | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    EngineMode: StrictStr | None = None
    ScalingConfiguration: RDSScalingConfigurationModel | None = None
    DBClusterParameterGroupName: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    Domain: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    DBClusterInstanceClass: StrictStr | None = None
    StorageType: StrictStr | None = None
    Iops: StrictInt | None = None
    PubliclyAccessible: StrictBool | None = None
    NetworkType: StrictStr | None = None
    ServerlessV2ScalingConfiguration: RDSServerlessV2ScalingConfigurationModel | None = None
    RdsCustomClusterConfiguration: _RdsCustomClusterConfigurationType | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    EngineLifecycleSupport: StrictStr | None = None
    TagSpecifications: list[RDSTagSpecificationModel] | None = None
    EnableVPCNetworking: StrictBool | None = None
    EnableInternetAccessGateway: StrictBool | None = None
    AssociatedRoles: list[RDSDBClusterAssociatedRoleModel] | None = None
