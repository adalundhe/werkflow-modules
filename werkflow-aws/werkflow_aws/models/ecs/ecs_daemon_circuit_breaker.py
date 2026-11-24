from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSDaemonCircuitBreaker(BaseModel):
    failureCount: StrictInt | None = None
    status: StrictStr | None = None
    threshold: StrictInt | None = None
