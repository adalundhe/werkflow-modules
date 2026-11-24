from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_backup_details import DynamoDBBackupDetails


class DynamoDBCreateBackupResponse(BaseModel):
    BackupDetails: DynamoDBBackupDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
