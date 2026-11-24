from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DataZoneDeploymentProperties(BaseModel):
    startTimeoutMinutes: StrictInt | None = None
    endTimeoutMinutes: StrictInt | None = None
