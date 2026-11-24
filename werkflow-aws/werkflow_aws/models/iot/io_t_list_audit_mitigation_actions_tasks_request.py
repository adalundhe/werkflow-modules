from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListAuditMitigationActionsTasksRequest(BaseModel):
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    auditTaskId: StrictStr | None = None
    findingId: StrictStr | None = None
    taskStatus: Literal['IN_PROGRESS', 'COMPLETED', 'FAILED', 'CANCELED'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
