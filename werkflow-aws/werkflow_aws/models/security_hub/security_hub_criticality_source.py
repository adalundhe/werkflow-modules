from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubCriticalitySource(BaseModel):
    Source: StrictStr | None = None
    Reason: StrictStr | None = None
