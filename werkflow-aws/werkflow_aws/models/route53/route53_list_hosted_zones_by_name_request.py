from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListHostedZonesByNameRequest(BaseModel):
    DNSName: StrictStr | None = None
    HostedZoneId: StrictStr | None = None
    MaxItems: StrictStr | None = None
