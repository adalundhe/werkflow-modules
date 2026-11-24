from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_environment_error import DataZoneEnvironmentError


class DataZoneDeployment(BaseModel):
    deploymentId: StrictStr | None = None
    deploymentType: StrictStr | None = None
    deploymentStatus: StrictStr | None = None
    failureReason: DataZoneEnvironmentError | None = None
    messages: list[StrictStr] | None = None
    isDeploymentComplete: StrictBool | None = None
