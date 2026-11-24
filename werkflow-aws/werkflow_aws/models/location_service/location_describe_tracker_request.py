from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDescribeTrackerRequest(BaseModel):
    TrackerName: StrictStr
