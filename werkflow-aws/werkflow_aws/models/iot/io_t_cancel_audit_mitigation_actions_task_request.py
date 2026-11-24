from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCancelAuditMitigationActionsTaskRequest(BaseModel):
    taskId: StrictStr
