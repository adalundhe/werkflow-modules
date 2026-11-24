from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCreateDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    DBInstanceClass: StrictStr
    Engine: StrictStr
    DBClusterIdentifier: StrictStr
    DBName: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
    DBSecurityGroups: list[StrictStr] | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    AvailabilityZone: StrictStr | None = None
    DBSubnetGroupName: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    DBParameterGroupName: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    Port: StrictInt | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    OptionGroupName: StrictStr | None = None
    CharacterSetName: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    Tags: list[NeptuneTag] | None = None
    StorageType: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    TdeCredentialPassword: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    Domain: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    MonitoringInterval: StrictInt | None = None
    MonitoringRoleArn: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    PromotionTier: StrictInt | None = None
    Timezone: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    EnablePerformanceInsights: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    DeletionProtection: StrictBool | None = None
