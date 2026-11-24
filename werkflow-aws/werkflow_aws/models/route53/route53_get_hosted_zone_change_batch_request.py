from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53GetHostedZoneChangeBatchRequest(BaseModel):
    HostedZoneId: StrictStr
    ChangeId: StrictStr
