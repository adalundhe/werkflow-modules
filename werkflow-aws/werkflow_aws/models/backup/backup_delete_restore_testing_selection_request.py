from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteRestoreTestingSelectionRequest(BaseModel):
    RestoreTestingPlanName: StrictStr
    RestoreTestingSelectionName: StrictStr
