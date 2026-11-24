from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailAvailabilityZone(BaseModel):
    zoneName: StrictStr | None = None
    state: StrictStr | None = None
