from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictFloat, StrictInt
from .location_circle import LocationCircle


class LocationGeofenceGeometry(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Polygon: list[list[list[StrictFloat | StrictInt]]] | None = None
    Circle: LocationCircle | None = None
    Geobuf: StrictBytes | Any | None = None
    MultiPolygon: list[list[list[list[StrictFloat | StrictInt]]]] | None = None
