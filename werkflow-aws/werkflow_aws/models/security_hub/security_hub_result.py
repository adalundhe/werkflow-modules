from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubResult(BaseModel):
    AccountId: StrictStr | None = None
    ProcessingResult: StrictStr | None = None
