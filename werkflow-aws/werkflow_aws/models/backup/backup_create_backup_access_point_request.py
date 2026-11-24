from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupCreateBackupAccessPointRequest(BaseModel):
    Name: StrictStr
    RecoveryPointArn: StrictStr
    AccessPointMetadata: dict[StrictStr, StrictStr] | None = None
    AccessPointPolicy: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
