from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightGeospatialCoordinateBounds(BaseModel):
    North: StrictFloat | StrictInt | None = None
    South: StrictFloat | StrictInt | None = None
    West: StrictFloat | StrictInt | None = None
    East: StrictFloat | StrictInt | None = None
