from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListBackupAccessPointsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
