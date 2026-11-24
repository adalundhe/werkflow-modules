from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LocationListTrackerConsumersRequest(BaseModel):
    TrackerName: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
