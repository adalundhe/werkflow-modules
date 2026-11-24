from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSRoute(BaseModel):
    DestinationType: StrictStr | None = None
    TargetType: StrictStr | None = None
    Destination: StrictStr | None = None
    Target: StrictStr | None = None
