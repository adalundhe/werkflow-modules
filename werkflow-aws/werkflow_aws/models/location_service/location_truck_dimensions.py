from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationTruckDimensions(BaseModel):
    Length: StrictFloat | StrictInt | None = None
    Height: StrictFloat | StrictInt | None = None
    Width: StrictFloat | StrictInt | None = None
    Unit: Literal['Meters', 'Feet'] | None = None
