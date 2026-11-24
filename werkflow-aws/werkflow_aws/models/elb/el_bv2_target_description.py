from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2TargetDescription(BaseModel):
    Id: StrictStr | None = None
    Port: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    QuicServerId: StrictStr | None = None
