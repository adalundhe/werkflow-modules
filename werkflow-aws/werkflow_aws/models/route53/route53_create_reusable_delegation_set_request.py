from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53CreateReusableDelegationSetRequest(BaseModel):
    CallerReference: StrictStr
    HostedZoneId: StrictStr | None = None
