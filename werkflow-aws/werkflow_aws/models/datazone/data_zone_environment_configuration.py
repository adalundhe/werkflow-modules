from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_aws_account import DataZoneAwsAccount
from .data_zone_environment_configuration_parameters_details import DataZoneEnvironmentConfigurationParametersDetails
from .data_zone_region import DataZoneRegion


class DataZoneEnvironmentConfiguration(BaseModel):
    name: StrictStr | None = None
    id: StrictStr | None = None
    environmentBlueprintId: StrictStr | None = None
    description: StrictStr | None = None
    deploymentMode: StrictStr | None = None
    configurationParameters: DataZoneEnvironmentConfigurationParametersDetails | None = None
    awsAccount: DataZoneAwsAccount | None = None
    accountPools: list[StrictStr] | None = None
    awsRegion: DataZoneRegion | None = None
    deploymentOrder: StrictInt | None = None
