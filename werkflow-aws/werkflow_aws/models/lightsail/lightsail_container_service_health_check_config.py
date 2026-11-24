from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailContainerServiceHealthCheckConfig(BaseModel):
    healthyThreshold: StrictInt | None = None
    unhealthyThreshold: StrictInt | None = None
    timeoutSeconds: StrictInt | None = None
    intervalSeconds: StrictInt | None = None
    path: StrictStr | None = None
    successCodes: StrictStr | None = None
