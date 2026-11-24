from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListBackupAccessPointsByRecoveryPointRequest(BaseModel):
    RecoveryPointArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
