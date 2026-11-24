from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53HostedZoneOwner(BaseModel):
    OwningAccount: StrictStr | None = None
    OwningService: StrictStr | None = None
