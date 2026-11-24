from __future__ import annotations
from typing import Literal


Route53RRType = Literal[
    'SOA',
    'A',
    'TXT',
    'NS',
    'CNAME',
    'MX',
    'NAPTR',
    'PTR',
    'SRV',
    'SPF',
    'AAAA',
    'CAA',
    'DS',
    'TLSA',
    'SSHFP',
    'SVCB',
    'HTTPS',
]
