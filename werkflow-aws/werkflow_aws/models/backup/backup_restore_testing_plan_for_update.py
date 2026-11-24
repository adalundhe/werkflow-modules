from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .backup_restore_testing_recovery_point_selection import BackupRestoreTestingRecoveryPointSelection


class BackupRestoreTestingPlanForUpdate(BaseModel):
    RecoveryPointSelection: BackupRestoreTestingRecoveryPointSelection | None = None
    ScheduleExpression: StrictStr | None = None
    ScheduleExpressionTimezone: StrictStr | None = None
    StartWindowHours: StrictInt | None = None
