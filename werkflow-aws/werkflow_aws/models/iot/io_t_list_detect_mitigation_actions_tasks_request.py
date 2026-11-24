from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListDetectMitigationActionsTasksRequest(BaseModel):
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
