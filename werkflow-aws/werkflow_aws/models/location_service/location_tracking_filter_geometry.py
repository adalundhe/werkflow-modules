from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationTrackingFilterGeometry(BaseModel):
    Polygon: list[list[list[StrictFloat | StrictInt]]] | None = None
