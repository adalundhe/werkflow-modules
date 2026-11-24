from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightGeospatialCircleRadius(BaseModel):
    Radius: StrictFloat | StrictInt | None = None
