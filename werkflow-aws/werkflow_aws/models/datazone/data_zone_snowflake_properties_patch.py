from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_connectivity_properties_patch import DataZoneConnectivityPropertiesPatch
from .data_zone_lineage_sync_input import DataZoneLineageSyncInput


class DataZoneSnowflakePropertiesPatch(BaseModel):
    connectivityPropertiesPatch: DataZoneConnectivityPropertiesPatch | None = None
    snowflakeRole: StrictStr | None = None
    lineageSync: DataZoneLineageSyncInput | None = None
