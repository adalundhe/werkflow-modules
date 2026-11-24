from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListHostedZonesByVPCRequest(BaseModel):
    VPCId: StrictStr
    VPCRegion: StrictStr
    MaxItems: StrictStr | None = None
    NextToken: StrictStr | None = None
