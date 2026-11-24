from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListRestoreTestingSelectionsRequest(BaseModel):
    RestoreTestingPlanName: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
