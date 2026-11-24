from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_plan_input import BackupPlanInput


class BackupUpdateBackupPlanRequest(BaseModel):
    BackupPlanId: StrictStr
    BackupPlan: BackupPlanInput
