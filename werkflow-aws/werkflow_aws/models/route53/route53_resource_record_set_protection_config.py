from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53ResourceRecordSetProtectionConfig(BaseModel):
    RecordName: StrictStr
    RecordType: Literal['SOA', 'A', 'TXT', 'NS', 'CNAME', 'MX', 'NAPTR', 'PTR', 'SRV', 'SPF', 'AAAA', 'CAA', 'DS', 'TLSA', 'SSHFP', 'SVCB', 'HTTPS']
    Comment: StrictStr | None = None
