from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53GetDNSSECRequest(BaseModel):
    HostedZoneId: StrictStr
