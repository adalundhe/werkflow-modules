from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionPoint(BaseModel):
    X: StrictFloat | StrictInt | None = None
    Y: StrictFloat | StrictInt | None = None
