from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DnsOptions(BaseModel):
    DnsRecordIpType: StrictStr | None = None
    PrivateDnsOnlyForInboundResolverEndpoint: StrictBool | None = None
    PrivateDnsPreference: StrictStr | None = None
    PrivateDnsSpecifiedDomains: list[StrictStr] | None = None
