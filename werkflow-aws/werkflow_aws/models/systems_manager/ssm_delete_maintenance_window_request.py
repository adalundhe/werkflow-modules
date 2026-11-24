from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeleteMaintenanceWindowRequest(BaseModel):
    WindowId: StrictStr
