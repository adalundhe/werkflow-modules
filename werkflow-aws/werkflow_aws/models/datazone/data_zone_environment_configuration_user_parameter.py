from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_environment_parameter import DataZoneEnvironmentParameter
from .data_zone_environment_resolved_account import DataZoneEnvironmentResolvedAccount


class DataZoneEnvironmentConfigurationUserParameter(BaseModel):
    environmentId: StrictStr | None = None
    environmentBlueprintId: StrictStr | None = None
    environmentResolvedAccount: DataZoneEnvironmentResolvedAccount | None = None
    environmentConfigurationName: StrictStr | None = None
    environmentParameters: list[DataZoneEnvironmentParameter] | None = None
