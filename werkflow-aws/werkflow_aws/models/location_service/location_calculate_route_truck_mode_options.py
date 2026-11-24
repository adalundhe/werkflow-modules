from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .location_truck_dimensions import LocationTruckDimensions
from .location_truck_weight import LocationTruckWeight


class LocationCalculateRouteTruckModeOptions(BaseModel):
    AvoidFerries: StrictBool | None = None
    AvoidTolls: StrictBool | None = None
    Dimensions: LocationTruckDimensions | None = None
    Weight: LocationTruckWeight | None = None
