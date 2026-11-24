from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_restore_testing_plan_for_list import BackupRestoreTestingPlanForList


class BackupListRestoreTestingPlansResponse(BaseModel):
    NextToken: StrictStr | None = None
    RestoreTestingPlans: list[BackupRestoreTestingPlanForList] | None = None
    ResponseMetadata: dict[str, Any] | None = None
