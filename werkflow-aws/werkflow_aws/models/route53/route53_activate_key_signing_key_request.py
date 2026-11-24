from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ActivateKeySigningKeyRequest(BaseModel):
    HostedZoneId: StrictStr
    Name: StrictStr
