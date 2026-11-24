from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DeactivateKeySigningKeyRequest(BaseModel):
    HostedZoneId: StrictStr
    Name: StrictStr
