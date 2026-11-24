from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53CreateKeySigningKeyRequest(BaseModel):
    CallerReference: StrictStr
    HostedZoneId: StrictStr
    KeyManagementServiceArn: StrictStr
    Name: StrictStr
    Status: StrictStr
