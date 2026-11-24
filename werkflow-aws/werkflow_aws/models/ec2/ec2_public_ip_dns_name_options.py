from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PublicIpDnsNameOptions(BaseModel):
    DnsHostnameType: StrictStr | None = None
    PublicIpv4DnsName: StrictStr | None = None
    PublicIpv6DnsName: StrictStr | None = None
    PublicDualStackDnsName: StrictStr | None = None
