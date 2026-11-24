from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListDetectMitigationActionsExecutionsRequest(BaseModel):
    taskId: StrictStr | None = None
    violationId: StrictStr | None = None
    thingName: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
