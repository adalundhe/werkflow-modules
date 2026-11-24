from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_plan_input import BackupPlanInput


class BackupCreateBackupPlanRequest(BaseModel):
    BackupPlan: BackupPlanInput
    BackupPlanTags: dict[StrictStr, StrictStr] | None = None
    CreatorRequestId: StrictStr | None = None
