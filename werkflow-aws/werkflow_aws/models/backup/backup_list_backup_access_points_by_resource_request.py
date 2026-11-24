from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListBackupAccessPointsByResourceRequest(BaseModel):
    ResourceArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
