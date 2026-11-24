from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DnsOptionsSpecification(BaseModel):
    DnsRecordIpType: Literal['ipv4', 'dualstack', 'ipv6', 'service-defined'] | None = None
    PrivateDnsOnlyForInboundResolverEndpoint: StrictBool | None = None
    PrivateDnsPreference: StrictStr | None = None
    PrivateDnsSpecifiedDomains: list[StrictStr] | None = None
