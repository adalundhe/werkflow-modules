from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueExecutionAttempt(BaseModel):
    Status: StrictStr | None = None
    ColumnStatisticsTaskRunId: StrictStr | None = None
    ExecutionTimestamp: datetime.datetime | StrictStr | None = None
    ErrorMessage: StrictStr | None = None
