from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .open_search_auto_tune_maintenance_schedule import OpenSearchAutoTuneMaintenanceSchedule


class OpenSearchAutoTuneOptions(BaseModel):
    DesiredState: StrictStr | None = None
    RollbackOnDisable: StrictStr | None = None
    MaintenanceSchedules: list[OpenSearchAutoTuneMaintenanceSchedule] | None = None
    UseOffPeakWindow: StrictBool | None = None
