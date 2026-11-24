from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTMaintenanceWindow(BaseModel):
    startTime: StrictStr | None = None
    durationInMinutes: StrictInt | None = None
