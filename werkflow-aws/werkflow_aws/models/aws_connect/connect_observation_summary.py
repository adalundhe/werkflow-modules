from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConnectObservationSummary(BaseModel):
    TotalObservations: StrictInt | None = None
    ObservationsPassed: StrictInt | None = None
    ObservationsFailed: StrictInt | None = None
