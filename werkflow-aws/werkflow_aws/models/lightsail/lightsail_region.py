from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_availability_zone import LightsailAvailabilityZone


class LightsailRegion(BaseModel):
    continentCode: StrictStr | None = None
    description: StrictStr | None = None
    displayName: StrictStr | None = None
    name: StrictStr | None = None
    availabilityZones: list[LightsailAvailabilityZone] | None = None
    relationalDatabaseAvailabilityZones: list[LightsailAvailabilityZone] | None = None
