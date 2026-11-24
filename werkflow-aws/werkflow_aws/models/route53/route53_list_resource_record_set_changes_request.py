from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53ListResourceRecordSetChangesRequest(BaseModel):
    HostedZoneId: StrictStr
    RecordName: StrictStr | None = None
    RecordType: Literal['SOA', 'A', 'TXT', 'NS', 'CNAME', 'MX', 'NAPTR', 'PTR', 'SRV', 'SPF', 'AAAA', 'CAA', 'DS', 'TLSA', 'SSHFP', 'SVCB', 'HTTPS'] | None = None
    SubmittedAfter: StrictStr | None = None
    SubmittedBefore: StrictStr | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
