from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_backup_summary import DynamoDBBackupSummary


class DynamoDBListBackupsResponse(BaseModel):
    BackupSummaries: list[DynamoDBBackupSummary] | None = None
    LastEvaluatedBackupArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
