from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LightsailGetRegionsRequest(BaseModel):
    includeAvailabilityZones: StrictBool | None = None
    includeRelationalDatabaseAvailabilityZones: StrictBool | None = None
