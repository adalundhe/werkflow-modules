from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetMaintenanceWindowExecutionTaskInvocationRequest(BaseModel):
    WindowExecutionId: StrictStr
    TaskId: StrictStr
    InvocationId: StrictStr
