from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSPrimaryEndpoint(BaseModel):
    Address: StrictStr | None = None
    HostedZoneId: StrictStr | None = None
