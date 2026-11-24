from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSServiceDeploymentCircuitBreaker(BaseModel):
    status: StrictStr | None = None
    failureCount: StrictInt | None = None
    threshold: StrictInt | None = None
