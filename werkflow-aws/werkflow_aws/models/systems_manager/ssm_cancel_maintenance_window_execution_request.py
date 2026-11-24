from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMCancelMaintenanceWindowExecutionRequest(BaseModel):
    WindowExecutionId: StrictStr
