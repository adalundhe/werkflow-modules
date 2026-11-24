from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionBlackFrame(BaseModel):
    MaxPixelThreshold: StrictFloat | StrictInt | None = None
    MinCoveragePercentage: StrictFloat | StrictInt | None = None
