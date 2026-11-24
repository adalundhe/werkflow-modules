from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationCircle(BaseModel):
    Center: list[StrictFloat | StrictInt] | None = None
    Radius: StrictFloat | StrictInt | None = None
