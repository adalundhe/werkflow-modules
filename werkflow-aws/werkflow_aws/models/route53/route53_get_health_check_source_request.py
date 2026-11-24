from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53GetHealthCheckSourceRequest(BaseModel):
    HealthCheckSourceId: StrictStr
