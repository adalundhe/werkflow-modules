from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_connectivity_properties import DataZoneConnectivityProperties
from .data_zone_identity_mapping import DataZoneIdentityMapping
from .data_zone_lineage_sync_input import DataZoneLineageSyncInput


class DataZoneSnowflakePropertiesInput(BaseModel):
    snowflakeRole: StrictStr
    identityMapping: DataZoneIdentityMapping
    connectivityProperties: DataZoneConnectivityProperties | None = None
    lineageSync: DataZoneLineageSyncInput | None = None
