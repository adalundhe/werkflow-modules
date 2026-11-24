from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetMaintenanceWindowRequest(BaseModel):
    WindowId: StrictStr
