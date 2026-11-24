from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .data_zone_lineage_sync_schedule import DataZoneLineageSyncSchedule


class DataZoneRedshiftLineageSyncConfigurationInput(BaseModel):
    enabled: StrictBool | None = None
    schedule: DataZoneLineageSyncSchedule | None = None
