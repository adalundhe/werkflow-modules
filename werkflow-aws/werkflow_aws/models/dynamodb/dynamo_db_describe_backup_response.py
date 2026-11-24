from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_backup_description import DynamoDBBackupDescription


class DynamoDBDescribeBackupResponse(BaseModel):
    BackupDescription: DynamoDBBackupDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
