from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .location_leg_geometry import LocationLegGeometry
from .location_step import LocationStep


class LocationLeg(BaseModel):
    StartPosition: list[StrictFloat | StrictInt] | None = None
    EndPosition: list[StrictFloat | StrictInt] | None = None
    Distance: StrictFloat | StrictInt | None = None
    DurationSeconds: StrictFloat | StrictInt | None = None
    Geometry: LocationLegGeometry | None = None
    Steps: list[LocationStep] | None = None
