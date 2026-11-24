from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_identity_mapping import DataZoneIdentityMapping
from .data_zone_lineage_sync_output import DataZoneLineageSyncOutput


class DataZoneSnowflakePropertiesOutput(BaseModel):
    snowflakeRole: StrictStr | None = None
    identityMapping: DataZoneIdentityMapping | None = None
    lineageSync: DataZoneLineageSyncOutput | None = None
    status: StrictStr | None = None
    errorMessage: StrictStr | None = None
