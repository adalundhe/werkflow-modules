from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetMaintenanceWindowExecutionRequest(BaseModel):
    WindowExecutionId: StrictStr
