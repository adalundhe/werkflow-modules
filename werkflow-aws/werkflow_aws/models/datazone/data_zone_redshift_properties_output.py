from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_redshift_credentials import DataZoneRedshiftCredentials
from .data_zone_redshift_lineage_sync_configuration_output import DataZoneRedshiftLineageSyncConfigurationOutput
from .data_zone_redshift_storage_properties import DataZoneRedshiftStorageProperties


class DataZoneRedshiftPropertiesOutput(BaseModel):
    storage: DataZoneRedshiftStorageProperties | None = None
    credentials: DataZoneRedshiftCredentials | None = None
    isProvisionedSecret: StrictBool | None = None
    jdbcIamUrl: StrictStr | None = None
    jdbcUrl: StrictStr | None = None
    redshiftTempDir: StrictStr | None = None
    lineageSync: DataZoneRedshiftLineageSyncConfigurationOutput | None = None
    status: StrictStr | None = None
    databaseName: StrictStr | None = None
