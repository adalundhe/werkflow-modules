from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTCommandExecutionSummary(BaseModel):
    commandArn: StrictStr | None = None
    executionId: StrictStr | None = None
    targetArn: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    completedAt: datetime.datetime | StrictStr | None = None
