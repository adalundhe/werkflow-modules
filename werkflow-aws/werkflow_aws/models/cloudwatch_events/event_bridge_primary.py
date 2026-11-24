from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgePrimary(BaseModel):
    HealthCheck: StrictStr | None = None
