from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TimeTrackingDetails(BaseModel):
    originalEstimate: StrictStr | None = None
    originalEstimateSeconds: StrictInt | None = None
    remainingEstimate: StrictStr | None = None
    remainingEstimateSeconds: StrictInt | None = None
    timeSpent: StrictStr | None = None
    timeSpentSeconds: StrictInt | None = None
