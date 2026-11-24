from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTAuditMitigationActionsTaskMetadata(BaseModel):
    taskId: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    taskStatus: StrictStr | None = None
