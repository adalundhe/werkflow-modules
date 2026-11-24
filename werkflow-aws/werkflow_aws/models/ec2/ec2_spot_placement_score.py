from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2SpotPlacementScore(BaseModel):
    Region: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Score: StrictInt | None = None
