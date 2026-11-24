from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .pinpoint_gps_coordinates import PinpointGPSCoordinates


class PinpointGPSPointDimension(BaseModel):
    Coordinates: PinpointGPSCoordinates | None = None
    RangeInKilometers: StrictFloat | StrictInt | None = None
