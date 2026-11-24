from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeBackupRequest(BaseModel):
    BackupArn: StrictStr
