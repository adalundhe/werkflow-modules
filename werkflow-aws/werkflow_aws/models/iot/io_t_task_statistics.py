from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IoTTaskStatistics(BaseModel):
    totalChecks: StrictInt | None = None
    inProgressChecks: StrictInt | None = None
    waitingForDataCollectionChecks: StrictInt | None = None
    compliantChecks: StrictInt | None = None
    nonCompliantChecks: StrictInt | None = None
    failedChecks: StrictInt | None = None
    canceledChecks: StrictInt | None = None
