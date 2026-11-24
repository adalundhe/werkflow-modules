from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeAuditMitigationActionsTaskRequest(BaseModel):
    taskId: StrictStr
