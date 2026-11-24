from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_cloudwatch_logs_export_configuration import DocumentDBCloudwatchLogsExportConfiguration
from .document_db_serverless_v2_scaling_configuration import DocumentDBServerlessV2ScalingConfiguration


class DocumentDBModifyDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    NewDBClusterIdentifier: StrictStr | None = None
    ApplyImmediately: StrictBool | None = None
    BackupRetentionPeriod: StrictInt | None = None
    DBClusterParameterGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    Port: StrictInt | None = None
    MasterUserPassword: StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    CloudwatchLogsExportConfiguration: DocumentDBCloudwatchLogsExportConfiguration | None = None
    EngineVersion: StrictStr | None = None
    AllowMajorVersionUpgrade: StrictBool | None = None
    DeletionProtection: StrictBool | None = None
    StorageType: StrictStr | None = None
    ServerlessV2ScalingConfiguration: DocumentDBServerlessV2ScalingConfiguration | None = None
    ManageMasterUserPassword: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
    RotateMasterUserPassword: StrictBool | None = None
    NetworkType: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
