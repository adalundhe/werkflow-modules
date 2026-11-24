from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_pending_cloudwatch_logs_exports import DocumentDBPendingCloudwatchLogsExports


class DocumentDBPendingModifiedValues(BaseModel):
    DBInstanceClass: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    MasterUserPassword: StrictStr | None = None
    Port: StrictInt | None = None
    BackupRetentionPeriod: StrictInt | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    Iops: StrictInt | None = None
    DBInstanceIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    DBSubnetGroupName: StrictStr | None = None
    PendingCloudwatchLogsExports: DocumentDBPendingCloudwatchLogsExports | None = None
