from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyLocalIpDetails(BaseModel):
    IpAddressV4: StrictStr | None = None
    IpAddressV6: StrictStr | None = None
