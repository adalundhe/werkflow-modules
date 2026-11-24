from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyThrottlingReason(BaseModel):
    reason: StrictStr | None = None
    resource: StrictStr | None = None
