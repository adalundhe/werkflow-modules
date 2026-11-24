from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAdjustment(BaseModel):
    Metric: StrictStr | None = None
    Reason: StrictStr | None = None
