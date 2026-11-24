from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_cloudwatch_logs_export_configuration import NeptuneCloudwatchLogsExportConfiguration


class NeptuneModifyDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    AllocatedStorage: StrictInt | None = None
    DBInstanceClass: StrictStr | None = None
    DBSubnetGroupName: StrictStr | None = None
    DBSecurityGroups: list[StrictStr] | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    ApplyImmediately: StrictBool | None = None
    MasterUserPassword: StrictStr | None = None
    DBParameterGroupName: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AllowMajorVersionUpgrade: StrictBool | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    OptionGroupName: StrictStr | None = None
    NewDBInstanceIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    TdeCredentialPassword: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    Domain: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    DBPortNumber: StrictInt | None = None
    PubliclyAccessible: StrictBool | None = None
    MonitoringRoleArn: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    PromotionTier: StrictInt | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    CloudwatchLogsExportConfiguration: NeptuneCloudwatchLogsExportConfiguration | None = None
    DeletionProtection: StrictBool | None = None
