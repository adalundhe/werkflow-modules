from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class BackupRestoreTestingPlanForList(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    LastExecutionTime: datetime.datetime | StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    RestoreTestingPlanArn: StrictStr | None = None
    RestoreTestingPlanName: StrictStr | None = None
    ScheduleExpression: StrictStr | None = None
    ScheduleExpressionTimezone: StrictStr | None = None
    StartWindowHours: StrictInt | None = None
