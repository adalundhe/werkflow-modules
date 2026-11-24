from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSDaemonCapacityProvider(BaseModel):
    arn: StrictStr | None = None
    runningCount: StrictInt | None = None
    withoutDaemonCount: StrictInt | None = None
