from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionStartShotDetectionFilter(BaseModel):
    MinSegmentConfidence: StrictFloat | StrictInt | None = None
