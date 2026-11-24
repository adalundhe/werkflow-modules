from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDeleteTrackerRequest(BaseModel):
    TrackerName: StrictStr
