from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .backup_restore_testing_recovery_point_selection import BackupRestoreTestingRecoveryPointSelection


class BackupRestoreTestingPlanForGet(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatorRequestId: StrictStr | None = None
    LastExecutionTime: datetime.datetime | StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    RecoveryPointSelection: BackupRestoreTestingRecoveryPointSelection | None = None
    RestoreTestingPlanArn: StrictStr | None = None
    RestoreTestingPlanName: StrictStr | None = None
    ScheduleExpression: StrictStr | None = None
    ScheduleExpressionTimezone: StrictStr | None = None
    StartWindowHours: StrictInt | None = None
