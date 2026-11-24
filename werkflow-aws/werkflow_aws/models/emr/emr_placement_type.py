from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRPlacementType(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZones: list[StrictStr] | None = None
