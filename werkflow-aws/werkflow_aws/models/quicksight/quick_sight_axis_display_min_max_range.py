from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightAxisDisplayMinMaxRange(BaseModel):
    Minimum: StrictFloat | StrictInt | None = None
    Maximum: StrictFloat | StrictInt | None = None
