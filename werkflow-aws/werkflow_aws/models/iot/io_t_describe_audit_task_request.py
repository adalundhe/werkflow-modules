from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeAuditTaskRequest(BaseModel):
    taskId: StrictStr
