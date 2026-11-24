from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionDetectionFilter(BaseModel):
    MinConfidence: StrictFloat | StrictInt | None = None
    MinBoundingBoxHeight: StrictFloat | StrictInt | None = None
    MinBoundingBoxWidth: StrictFloat | StrictInt | None = None
