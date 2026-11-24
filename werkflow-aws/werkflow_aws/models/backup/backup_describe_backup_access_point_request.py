from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeBackupAccessPointRequest(BaseModel):
    AccessPointArn: StrictStr
