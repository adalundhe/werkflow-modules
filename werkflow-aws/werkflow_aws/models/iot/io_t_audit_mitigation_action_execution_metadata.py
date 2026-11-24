from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTAuditMitigationActionExecutionMetadata(BaseModel):
    taskId: StrictStr | None = None
    findingId: StrictStr | None = None
    actionName: StrictStr | None = None
    actionId: StrictStr | None = None
    status: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    errorCode: StrictStr | None = None
    message: StrictStr | None = None
