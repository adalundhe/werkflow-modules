from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubDnsRequestAction(BaseModel):
    Domain: StrictStr | None = None
    Protocol: StrictStr | None = None
    Blocked: StrictBool | None = None
