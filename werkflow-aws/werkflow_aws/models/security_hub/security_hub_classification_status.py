from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubClassificationStatus(BaseModel):
    Code: StrictStr | None = None
    Reason: StrictStr | None = None
