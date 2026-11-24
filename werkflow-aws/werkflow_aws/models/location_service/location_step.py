from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationStep(BaseModel):
    StartPosition: list[StrictFloat | StrictInt] | None = None
    EndPosition: list[StrictFloat | StrictInt] | None = None
    Distance: StrictFloat | StrictInt | None = None
    DurationSeconds: StrictFloat | StrictInt | None = None
    GeometryOffset: StrictInt | None = None
