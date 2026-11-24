from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSPrimaryEndpointModel(BaseModel):
    Address: StrictStr | None = None
    HostedZoneId: StrictStr | None = None
