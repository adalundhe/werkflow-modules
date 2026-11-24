from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_redshift_credential_configuration import DataZoneRedshiftCredentialConfiguration
from .data_zone_redshift_storage import DataZoneRedshiftStorage
from .data_zone_relational_filter_configuration import DataZoneRelationalFilterConfiguration


class DataZoneRedshiftRunConfigurationOutput(BaseModel):
    accountId: StrictStr | None = None
    region: StrictStr | None = None
    dataAccessRole: StrictStr | None = None
    relationalFilterConfigurations: list[DataZoneRelationalFilterConfiguration] | None = None
    redshiftCredentialConfiguration: DataZoneRedshiftCredentialConfiguration | None = None
    redshiftStorage: DataZoneRedshiftStorage | None = None
