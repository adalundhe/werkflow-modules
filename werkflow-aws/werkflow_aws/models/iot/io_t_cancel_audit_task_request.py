from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCancelAuditTaskRequest(BaseModel):
    taskId: StrictStr
