from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_maintenance_window import IoTMaintenanceWindow


class IoTSchedulingConfig(BaseModel):
    startTime: StrictStr | None = None
    endTime: StrictStr | None = None
    endBehavior: StrictStr | None = None
    maintenanceWindows: list[IoTMaintenanceWindow] | None = None
