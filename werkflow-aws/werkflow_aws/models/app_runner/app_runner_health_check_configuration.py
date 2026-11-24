from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppRunnerHealthCheckConfiguration(BaseModel):
    Protocol: StrictStr | None = None
    Path: StrictStr | None = None
    Interval: StrictInt | None = None
    Timeout: StrictInt | None = None
    HealthyThreshold: StrictInt | None = None
    UnhealthyThreshold: StrictInt | None = None
