from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupGetRestoreTestingPlanRequest(BaseModel):
    RestoreTestingPlanName: StrictStr
