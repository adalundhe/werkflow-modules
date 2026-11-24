from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DeleteKeySigningKeyRequest(BaseModel):
    HostedZoneId: StrictStr
    Name: StrictStr
