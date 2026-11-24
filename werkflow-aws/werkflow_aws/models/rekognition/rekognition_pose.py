from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionPose(BaseModel):
    Roll: StrictFloat | StrictInt | None = None
    Yaw: StrictFloat | StrictInt | None = None
    Pitch: StrictFloat | StrictInt | None = None
