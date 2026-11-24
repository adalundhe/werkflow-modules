from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListBackupPlanVersionsRequest(BaseModel):
    BackupPlanId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
