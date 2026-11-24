from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBBackupSummary(BaseModel):
    TableName: StrictStr | None = None
    TableId: StrictStr | None = None
    TableArn: StrictStr | None = None
    BackupArn: StrictStr | None = None
    BackupName: StrictStr | None = None
    BackupCreationDateTime: datetime.datetime | StrictStr | None = None
    BackupExpiryDateTime: datetime.datetime | StrictStr | None = None
    BackupStatus: StrictStr | None = None
    BackupType: StrictStr | None = None
    BackupSizeBytes: StrictInt | None = None
