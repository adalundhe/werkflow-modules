from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTDetectMitigationActionExecution(BaseModel):
    taskId: StrictStr | None = None
    violationId: StrictStr | None = None
    actionName: StrictStr | None = None
    thingName: StrictStr | None = None
    executionStartDate: datetime.datetime | StrictStr | None = None
    executionEndDate: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    errorCode: StrictStr | None = None
    message: StrictStr | None = None
