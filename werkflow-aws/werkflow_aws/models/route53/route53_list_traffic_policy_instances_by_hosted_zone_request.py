from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53ListTrafficPolicyInstancesByHostedZoneRequest(BaseModel):
    HostedZoneId: StrictStr
    TrafficPolicyInstanceNameMarker: StrictStr | None = None
    TrafficPolicyInstanceTypeMarker: Literal['SOA', 'A', 'TXT', 'NS', 'CNAME', 'MX', 'NAPTR', 'PTR', 'SRV', 'SPF', 'AAAA', 'CAA', 'DS', 'TLSA', 'SSHFP', 'SVCB', 'HTTPS'] | None = None
    MaxItems: StrictStr | None = None
