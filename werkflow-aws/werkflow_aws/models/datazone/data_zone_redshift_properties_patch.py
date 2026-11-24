from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_redshift_credentials import DataZoneRedshiftCredentials
from .data_zone_redshift_lineage_sync_configuration_input import DataZoneRedshiftLineageSyncConfigurationInput
from .data_zone_redshift_storage_properties import DataZoneRedshiftStorageProperties


class DataZoneRedshiftPropertiesPatch(BaseModel):
    storage: DataZoneRedshiftStorageProperties | None = None
    databaseName: StrictStr | None = None
    host: StrictStr | None = None
    port: StrictInt | None = None
    credentials: DataZoneRedshiftCredentials | None = None
    lineageSync: DataZoneRedshiftLineageSyncConfigurationInput | None = None
