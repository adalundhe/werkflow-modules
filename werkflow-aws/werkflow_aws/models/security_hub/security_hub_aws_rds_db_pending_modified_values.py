from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_rds_db_processor_feature import SecurityHubAwsRdsDbProcessorFeature
from .security_hub_aws_rds_pending_cloud_watch_logs_exports import SecurityHubAwsRdsPendingCloudWatchLogsExports


class SecurityHubAwsRdsDbPendingModifiedValues(BaseModel):
    DbInstanceClass: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    MasterUserPassword: StrictStr | None = None
    Port: StrictInt | None = None
    BackupRetentionPeriod: StrictInt | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    DbInstanceIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    CaCertificateIdentifier: StrictStr | None = None
    DbSubnetGroupName: StrictStr | None = None
    PendingCloudWatchLogsExports: SecurityHubAwsRdsPendingCloudWatchLogsExports | None = None
    ProcessorFeatures: list[SecurityHubAwsRdsDbProcessorFeature] | None = None
