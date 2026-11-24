from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupGetBackupPlanRequest(BaseModel):
    BackupPlanId: StrictStr
    VersionId: StrictStr | None = None
    MaxScheduledRunsPreview: StrictInt | None = None
