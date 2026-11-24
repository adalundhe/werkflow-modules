from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupRestoreJobCreator(BaseModel):
    RestoreTestingPlanArn: StrictStr | None = None
