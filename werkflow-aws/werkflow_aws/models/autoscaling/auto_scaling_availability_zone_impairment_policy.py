from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingAvailabilityZoneImpairmentPolicy(BaseModel):
    ZonalShiftEnabled: StrictBool | None = None
    ImpairedZoneHealthCheckBehavior: StrictStr | None = None
