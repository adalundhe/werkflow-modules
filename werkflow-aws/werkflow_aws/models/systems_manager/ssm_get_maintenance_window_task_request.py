from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetMaintenanceWindowTaskRequest(BaseModel):
    WindowId: StrictStr
    WindowTaskId: StrictStr
