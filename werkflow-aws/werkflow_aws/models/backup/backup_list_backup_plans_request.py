from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class BackupListBackupPlansRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    IncludeDeleted: StrictBool | None = None
