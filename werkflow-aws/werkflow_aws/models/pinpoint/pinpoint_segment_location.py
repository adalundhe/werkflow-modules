from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_gps_point_dimension import PinpointGPSPointDimension
from .pinpoint_set_dimension import PinpointSetDimension


class PinpointSegmentLocation(BaseModel):
    Country: PinpointSetDimension | None = None
    GPSPoint: PinpointGPSPointDimension | None = None
