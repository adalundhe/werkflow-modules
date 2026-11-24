from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterInstancePlacement(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
