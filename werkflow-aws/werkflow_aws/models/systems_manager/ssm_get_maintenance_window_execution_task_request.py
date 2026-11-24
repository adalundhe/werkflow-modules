from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetMaintenanceWindowExecutionTaskRequest(BaseModel):
    WindowExecutionId: StrictStr
    TaskId: StrictStr
