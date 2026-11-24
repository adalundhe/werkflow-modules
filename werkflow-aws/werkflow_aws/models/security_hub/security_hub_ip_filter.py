from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubIpFilter(BaseModel):
    Cidr: StrictStr | None = None
