from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .backup_restore_testing_plan_for_get import BackupRestoreTestingPlanForGet


class BackupGetRestoreTestingPlanResponse(BaseModel):
    RestoreTestingPlan: BackupRestoreTestingPlanForGet | None = None
    ResponseMetadata: dict[str, Any] | None = None
