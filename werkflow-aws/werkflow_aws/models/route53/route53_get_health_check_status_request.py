from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53GetHealthCheckStatusRequest(BaseModel):
    HealthCheckId: StrictStr
