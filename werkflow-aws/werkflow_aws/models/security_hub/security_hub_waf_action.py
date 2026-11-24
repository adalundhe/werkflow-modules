from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubWafAction(BaseModel):
    Type: StrictStr | None = None
