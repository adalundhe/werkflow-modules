from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationPositionalAccuracy(BaseModel):
    Horizontal: StrictFloat | StrictInt | None = None
