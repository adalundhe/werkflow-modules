from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationForecastGeofenceEventsDeviceState(BaseModel):
    Position: list[StrictFloat | StrictInt]
    Speed: StrictFloat | StrictInt | None = None
