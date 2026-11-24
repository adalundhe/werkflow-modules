from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53TestDNSAnswerRequest(BaseModel):
    HostedZoneId: StrictStr
    RecordName: StrictStr
    RecordType: Literal['SOA', 'A', 'TXT', 'NS', 'CNAME', 'MX', 'NAPTR', 'PTR', 'SRV', 'SPF', 'AAAA', 'CAA', 'DS', 'TLSA', 'SSHFP', 'SVCB', 'HTTPS']
    ResolverIP: StrictStr | None = None
    EDNS0ClientSubnetIP: StrictStr | None = None
    EDNS0ClientSubnetMask: StrictStr | None = None
