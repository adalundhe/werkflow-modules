from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubActionLocalIpDetails(BaseModel):
    IpAddressV4: StrictStr | None = None
