from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class Route53HostedZoneConfigModel(BaseModel):
    Comment: StrictStr | None = None
    PrivateZone: StrictBool | None = None
    HostedZoneTier: StrictStr | None = None
