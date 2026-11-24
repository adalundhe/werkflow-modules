from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .location_route_matrix_entry_error import LocationRouteMatrixEntryError


class LocationRouteMatrixEntry(BaseModel):
    Distance: StrictFloat | StrictInt | None = None
    DurationSeconds: StrictFloat | StrictInt | None = None
    Error: LocationRouteMatrixEntryError | None = None
