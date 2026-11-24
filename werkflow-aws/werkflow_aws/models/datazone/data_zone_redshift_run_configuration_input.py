from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_redshift_credential_configuration import DataZoneRedshiftCredentialConfiguration
from .data_zone_redshift_storage import DataZoneRedshiftStorage
from .data_zone_relational_filter_configuration import DataZoneRelationalFilterConfiguration


class DataZoneRedshiftRunConfigurationInput(BaseModel):
    relationalFilterConfigurations: list[DataZoneRelationalFilterConfiguration]
    dataAccessRole: StrictStr | None = None
    redshiftCredentialConfiguration: DataZoneRedshiftCredentialConfiguration | None = None
    redshiftStorage: DataZoneRedshiftStorage | None = None
