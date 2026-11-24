from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_cloudwatch_logs_export_configuration import NeptuneCloudwatchLogsExportConfiguration
from .neptune_serverless_v2_scaling_configuration import NeptuneServerlessV2ScalingConfiguration


class NeptuneModifyDBClusterRequest(BaseModel):
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
    CloudwatchLogsExportConfiguration: NeptuneCloudwatchLogsExportConfiguration | None = None
    EngineVersion: StrictStr | None = None
    AllowMajorVersionUpgrade: StrictBool | None = None
    DBInstanceParameterGroupName: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    ServerlessV2ScalingConfiguration: NeptuneServerlessV2ScalingConfiguration | None = None
    StorageType: StrictStr | None = None
    NetworkType: StrictStr | None = None
