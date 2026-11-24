from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeregisterTaskFromMaintenanceWindowRequest(BaseModel):
    WindowId: StrictStr
    WindowTaskId: StrictStr
