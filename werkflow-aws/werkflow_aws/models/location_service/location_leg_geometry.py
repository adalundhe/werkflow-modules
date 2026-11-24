from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationLegGeometry(BaseModel):
    LineString: list[list[StrictFloat | StrictInt]] | None = None
