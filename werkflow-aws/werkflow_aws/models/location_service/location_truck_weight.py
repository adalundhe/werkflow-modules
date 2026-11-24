from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationTruckWeight(BaseModel):
    Total: StrictFloat | StrictInt | None = None
    Unit: Literal['Kilograms', 'Pounds'] | None = None
