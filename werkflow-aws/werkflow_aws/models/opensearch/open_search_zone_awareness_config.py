from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchZoneAwarenessConfig(BaseModel):
    AvailabilityZoneCount: StrictInt | None = None
