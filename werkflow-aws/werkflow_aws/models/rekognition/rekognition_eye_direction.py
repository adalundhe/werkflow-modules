from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionEyeDirection(BaseModel):
    Yaw: StrictFloat | StrictInt | None = None
    Pitch: StrictFloat | StrictInt | None = None
    Confidence: StrictFloat | StrictInt | None = None
