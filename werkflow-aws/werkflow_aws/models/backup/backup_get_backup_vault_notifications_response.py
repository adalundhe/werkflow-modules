from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BackupGetBackupVaultNotificationsResponse(BaseModel):
    BackupVaultName: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
    SNSTopicArn: StrictStr | None = None
    BackupVaultEvents: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
