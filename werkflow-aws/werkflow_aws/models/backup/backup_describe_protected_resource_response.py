from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class BackupDescribeProtectedResourceResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    ResourceType: StrictStr | None = None
    LastBackupTime: datetime.datetime | StrictStr | None = None
    ResourceName: StrictStr | None = None
    LastBackupVaultArn: StrictStr | None = None
    LastRecoveryPointArn: StrictStr | None = None
    LatestRestoreExecutionTimeMinutes: StrictInt | None = None
    LatestRestoreJobCreationDate: datetime.datetime | StrictStr | None = None
    LatestRestoreRecoveryPointCreationDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
