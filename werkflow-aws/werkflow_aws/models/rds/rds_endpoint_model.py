from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSEndpointModel(BaseModel):
    Address: StrictStr | None = None
    Port: StrictInt | None = None
    HostedZoneId: StrictStr | None = None
