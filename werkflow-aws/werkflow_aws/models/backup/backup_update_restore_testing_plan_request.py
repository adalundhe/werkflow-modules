from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_restore_testing_plan_for_update import BackupRestoreTestingPlanForUpdate


class BackupUpdateRestoreTestingPlanRequest(BaseModel):
    RestoreTestingPlan: BackupRestoreTestingPlanForUpdate
    RestoreTestingPlanName: StrictStr
