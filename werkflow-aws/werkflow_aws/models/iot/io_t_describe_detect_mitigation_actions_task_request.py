from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeDetectMitigationActionsTaskRequest(BaseModel):
    taskId: StrictStr
