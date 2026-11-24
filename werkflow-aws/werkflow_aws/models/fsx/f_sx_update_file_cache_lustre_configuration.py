from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxUpdateFileCacheLustreConfiguration(BaseModel):
    WeeklyMaintenanceStartTime: StrictStr | None = None
