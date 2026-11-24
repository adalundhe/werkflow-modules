from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionShotSegment(BaseModel):
    Index: StrictInt | None = None
    Confidence: StrictFloat | StrictInt | None = None
