from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailResourceLocation(BaseModel):
    availabilityZone: StrictStr | None = None
    regionName: StrictStr | None = None
