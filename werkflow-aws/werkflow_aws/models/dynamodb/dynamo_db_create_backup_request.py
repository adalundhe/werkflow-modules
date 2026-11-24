from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBCreateBackupRequest(BaseModel):
    TableName: StrictStr
    BackupName: StrictStr
