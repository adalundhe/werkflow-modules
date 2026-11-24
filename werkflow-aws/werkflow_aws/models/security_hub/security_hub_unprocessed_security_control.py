from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubUnprocessedSecurityControl(BaseModel):
    SecurityControlId: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorReason: StrictStr | None = None
