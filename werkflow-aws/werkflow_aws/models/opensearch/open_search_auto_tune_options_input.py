from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool
from .open_search_auto_tune_maintenance_schedule import OpenSearchAutoTuneMaintenanceSchedule


class OpenSearchAutoTuneOptionsInput(BaseModel):
    DesiredState: Literal['ENABLED', 'DISABLED'] | None = None
    MaintenanceSchedules: list[OpenSearchAutoTuneMaintenanceSchedule] | None = None
    UseOffPeakWindow: StrictBool | None = None
