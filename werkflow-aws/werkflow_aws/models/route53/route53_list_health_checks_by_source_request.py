from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListHealthChecksBySourceRequest(BaseModel):
    HealthCheckSourceId: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
