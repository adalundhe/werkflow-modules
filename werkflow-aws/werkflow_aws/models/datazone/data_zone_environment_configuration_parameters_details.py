from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_environment_configuration_parameter import DataZoneEnvironmentConfigurationParameter


class DataZoneEnvironmentConfigurationParametersDetails(BaseModel):
    ssmPath: StrictStr | None = None
    parameterOverrides: list[DataZoneEnvironmentConfigurationParameter] | None = None
    resolvedParameters: list[DataZoneEnvironmentConfigurationParameter] | None = None
