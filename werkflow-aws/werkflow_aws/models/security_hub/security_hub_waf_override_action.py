from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubWafOverrideAction(BaseModel):
    Type: StrictStr | None = None
