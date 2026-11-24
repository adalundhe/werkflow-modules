from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_restore_testing_plan_for_create import BackupRestoreTestingPlanForCreate


class BackupCreateRestoreTestingPlanRequest(BaseModel):
    RestoreTestingPlan: BackupRestoreTestingPlanForCreate
    CreatorRequestId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
