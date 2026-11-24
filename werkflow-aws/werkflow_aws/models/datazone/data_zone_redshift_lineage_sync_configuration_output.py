from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_lineage_sync_schedule import DataZoneLineageSyncSchedule


class DataZoneRedshiftLineageSyncConfigurationOutput(BaseModel):
    lineageJobId: StrictStr | None = None
    enabled: StrictBool | None = None
    schedule: DataZoneLineageSyncSchedule | None = None
