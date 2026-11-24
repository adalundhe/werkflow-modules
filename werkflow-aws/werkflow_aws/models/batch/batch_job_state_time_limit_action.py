from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchJobStateTimeLimitAction(BaseModel):
    reason: StrictStr | None = None
    state: StrictStr | None = None
    maxTimeSeconds: StrictInt | None = None
    action: StrictStr | None = None
