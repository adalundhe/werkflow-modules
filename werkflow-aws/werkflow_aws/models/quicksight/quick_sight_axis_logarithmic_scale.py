from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightAxisLogarithmicScale(BaseModel):
    Base: StrictFloat | StrictInt | None = None
