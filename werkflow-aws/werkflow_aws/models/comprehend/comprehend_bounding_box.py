from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ComprehendBoundingBox(BaseModel):
    Height: StrictFloat | StrictInt | None = None
    Left: StrictFloat | StrictInt | None = None
    Top: StrictFloat | StrictInt | None = None
    Width: StrictFloat | StrictInt | None = None
