from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SSMDeregisterTargetFromMaintenanceWindowRequest(BaseModel):
    WindowId: StrictStr
    WindowTargetId: StrictStr
    Safe: StrictBool | None = None
