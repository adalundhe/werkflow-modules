from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAuditTaskMetadata(BaseModel):
    taskId: StrictStr | None = None
    taskStatus: StrictStr | None = None
    taskType: StrictStr | None = None
