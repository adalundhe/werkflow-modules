from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .backup_restore_testing_recovery_point_selection import BackupRestoreTestingRecoveryPointSelection


class BackupRestoreTestingPlanForCreate(BaseModel):
    RecoveryPointSelection: BackupRestoreTestingRecoveryPointSelection
    RestoreTestingPlanName: StrictStr
    ScheduleExpression: StrictStr
    ScheduleExpressionTimezone: StrictStr | None = None
    StartWindowHours: StrictInt | None = None
