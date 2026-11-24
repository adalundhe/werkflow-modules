from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSDaemonDeploymentCapacityProvider(BaseModel):
    arn: StrictStr | None = None
    runningInstanceCount: StrictInt | None = None
    withoutDaemonInstanceCount: StrictInt | None = None
    drainingInstanceCount: StrictInt | None = None
