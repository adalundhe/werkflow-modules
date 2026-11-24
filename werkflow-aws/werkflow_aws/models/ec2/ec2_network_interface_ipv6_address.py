from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2NetworkInterfaceIpv6Address(BaseModel):
    Ipv6Address: StrictStr | None = None
    PublicIpv6DnsName: StrictStr | None = None
    IsPrimaryIpv6: StrictBool | None = None
