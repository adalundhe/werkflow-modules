from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53ListResourceRecordSetProtectionsRequest(BaseModel):
    HostedZoneId: StrictStr
    StartRecordName: StrictStr | None = None
    StartRecordType: Literal['SOA', 'A', 'TXT', 'NS', 'CNAME', 'MX', 'NAPTR', 'PTR', 'SRV', 'SPF', 'AAAA', 'CAA', 'DS', 'TLSA', 'SSHFP', 'SVCB', 'HTTPS'] | None = None
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
