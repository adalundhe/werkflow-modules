from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupPutBackupVaultNotificationsRequest(BaseModel):
    BackupVaultName: StrictStr
    SNSTopicArn: StrictStr
    BackupVaultEvents: list[StrictStr]
