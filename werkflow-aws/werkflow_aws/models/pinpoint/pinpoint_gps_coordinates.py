from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class PinpointGPSCoordinates(BaseModel):
    Latitude: StrictFloat | StrictInt | None = None
    Longitude: StrictFloat | StrictInt | None = None
