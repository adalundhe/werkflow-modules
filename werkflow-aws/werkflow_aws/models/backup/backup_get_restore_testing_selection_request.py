from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetRestoreTestingSelectionRequest(BaseModel):
    RestoreTestingPlanName: StrictStr
    RestoreTestingSelectionName: StrictStr
