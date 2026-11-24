from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_pending_cloudwatch_logs_exports import NeptunePendingCloudwatchLogsExports


class NeptuneClusterPendingModifiedValues(BaseModel):
    PendingCloudwatchLogsExports: NeptunePendingCloudwatchLogsExports | None = None
    DBClusterIdentifier: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    StorageType: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    Iops: StrictInt | None = None
    NetworkType: StrictStr | None = None
