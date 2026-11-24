from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBBackupDetails(BaseModel):
    BackupArn: StrictStr | None = None
    BackupName: StrictStr | None = None
    BackupSizeBytes: StrictInt | None = None
    BackupStatus: StrictStr | None = None
    BackupType: StrictStr | None = None
    BackupCreationDateTime: datetime.datetime | StrictStr | None = None
    BackupExpiryDateTime: datetime.datetime | StrictStr | None = None
