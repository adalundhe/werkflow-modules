from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsBackupBackupVaultNotificationsDetails(BaseModel):
    BackupVaultEvents: list[StrictStr] | None = None
    SnsTopicArn: StrictStr | None = None
