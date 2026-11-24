from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListAuditTasksRequest(BaseModel):
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    taskType: Literal['ON_DEMAND_AUDIT_TASK', 'SCHEDULED_AUDIT_TASK'] | None = None
    taskStatus: Literal['IN_PROGRESS', 'COMPLETED', 'FAILED', 'CANCELED'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
