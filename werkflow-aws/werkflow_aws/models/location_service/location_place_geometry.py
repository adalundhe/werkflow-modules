from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationPlaceGeometry(BaseModel):
    Point: list[StrictFloat | StrictInt] | None = None
