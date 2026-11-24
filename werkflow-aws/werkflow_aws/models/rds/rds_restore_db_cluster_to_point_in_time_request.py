from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rdsdb_cluster_associated_role_model import RDSDBClusterAssociatedRoleModel
from .rds_scaling_configuration_model import RDSScalingConfigurationModel
from .rds_serverless_v2_scaling_configuration_model import RDSServerlessV2ScalingConfigurationModel
from .rds_tag_model import RDSTagModel
from .rds_tag_specification_model import RDSTagSpecificationModel
from .rds_custom_cluster_configuration import RdsCustomClusterConfiguration as _RdsCustomClusterConfigurationType


class RDSRestoreDBClusterToPointInTimeRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    RestoreType: StrictStr | None = None
    SourceDBClusterIdentifier: StrictStr | None = None
    RestoreToTime: datetime.datetime | StrictStr | None = None
    UseLatestRestorableTime: StrictBool | None = None
    Port: StrictInt | None = None
    DBSubnetGroupName: StrictStr | None = None
    OptionGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    Tags: list[RDSTagModel] | None = None
    KmsKeyId: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    BacktrackWindow: StrictInt | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    DBClusterParameterGroupName: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    Domain: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    DBClusterInstanceClass: StrictStr | None = None
    StorageType: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    Iops: StrictInt | None = None
    NetworkType: StrictStr | None = None
    SourceDbClusterResourceId: StrictStr | None = None
    ServerlessV2ScalingConfiguration: RDSServerlessV2ScalingConfigurationModel | None = None
    ScalingConfiguration: RDSScalingConfigurationModel | None = None
    EngineMode: StrictStr | None = None
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
