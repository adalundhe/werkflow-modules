from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class IoTJobExecutionSummary(BaseModel):
    status: StrictStr | None = None
    queuedAt: datetime.datetime | StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    executionNumber: StrictInt | None = None
    retryAttempt: StrictInt | None = None
