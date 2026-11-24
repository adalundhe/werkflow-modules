from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DnsEntry(BaseModel):
    DnsName: StrictStr | None = None
    HostedZoneId: StrictStr | None = None
