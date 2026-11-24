from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53GetHostedZoneLimitRequest(BaseModel):
    Type: Literal['MAX_RRSETS_BY_ZONE', 'MAX_VPCS_ASSOCIATED_BY_ZONE']
    HostedZoneId: StrictStr
