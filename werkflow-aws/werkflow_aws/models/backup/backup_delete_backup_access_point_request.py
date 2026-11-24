from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteBackupAccessPointRequest(BaseModel):
    AccessPointArn: StrictStr
