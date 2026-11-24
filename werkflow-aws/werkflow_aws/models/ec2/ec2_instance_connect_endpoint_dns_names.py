from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceConnectEndpointDnsNames(BaseModel):
    DnsName: StrictStr | None = None
    FipsDnsName: StrictStr | None = None
