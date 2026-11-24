from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRemediationTrait(BaseModel):
    Type: StrictStr | None = None
    Title: StrictStr | None = None
