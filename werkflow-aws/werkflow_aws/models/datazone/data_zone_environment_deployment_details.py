from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_environment_error import DataZoneEnvironmentError


class DataZoneEnvironmentDeploymentDetails(BaseModel):
    overallDeploymentStatus: StrictStr | None = None
    environmentFailureReasons: dict[StrictStr, list[DataZoneEnvironmentError]] | None = None
