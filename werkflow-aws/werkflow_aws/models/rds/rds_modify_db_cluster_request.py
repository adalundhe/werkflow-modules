from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_cloudwatch_logs_export_configuration import RDSCloudwatchLogsExportConfiguration
from .rds_database_insights_mode import RDSDatabaseInsightsMode
from .rds_master_user_authentication_type import RDSMasterUserAuthenticationType
from .rds_scaling_configuration import RDSScalingConfiguration
from .rds_serverless_v2_scaling_configuration import RDSServerlessV2ScalingConfiguration


class RDSModifyDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    NewDBClusterIdentifier: StrictStr | None = None
    ApplyImmediately: StrictBool | None = None
    BackupRetentionPeriod: StrictInt | None = None
    DBClusterParameterGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    Port: StrictInt | None = None
    MasterUserPassword: StrictStr | None = None
    OptionGroupName: StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    BacktrackWindow: StrictInt | None = None
    CloudwatchLogsExportConfiguration: RDSCloudwatchLogsExportConfiguration | None = None
    EngineVersion: StrictStr | None = None
    AllowMajorVersionUpgrade: StrictBool | None = None
    DBInstanceParameterGroupName: StrictStr | None = None
    Domain: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    ScalingConfiguration: RDSScalingConfiguration | None = None
    DeletionProtection: StrictBool | None = None
    EnableHttpEndpoint: StrictBool | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    EnableGlobalWriteForwarding: StrictBool | None = None
    DBClusterInstanceClass: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    StorageType: StrictStr | None = None
    Iops: StrictInt | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    NetworkType: StrictStr | None = None
    ServerlessV2ScalingConfiguration: RDSServerlessV2ScalingConfiguration | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    DatabaseInsightsMode: RDSDatabaseInsightsMode | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    PerformanceInsightsRetentionPeriod: StrictInt | None = None
    ManageMasterUserPassword: StrictBool | None = None
    RotateMasterUserPassword: StrictBool | None = None
    EnableLocalWriteForwarding: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
    EngineMode: StrictStr | None = None
    AllowEngineModeChange: StrictBool | None = None
    AwsBackupRecoveryPointArn: StrictStr | None = None
    EnableLimitlessDatabase: StrictBool | None = None
    CACertificateIdentifier: StrictStr | None = None
    MasterUserAuthenticationType: RDSMasterUserAuthenticationType | None = None
    EngineLifecycleSupport: StrictStr | None = None
    EnableInternetAccessGateway: StrictBool | None = None
    EnableVPCNetworking: StrictBool | None = None
    DBSubnetGroupName: StrictStr | None = None
