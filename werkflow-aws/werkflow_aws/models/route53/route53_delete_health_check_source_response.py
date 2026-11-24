from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class Route53DeleteHealthCheckSourceResponse(BaseModel):
    HealthCheckSourceId: StrictStr | None = None
    HealthCheckSourceStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
