from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionImageQuality(BaseModel):
    Brightness: StrictFloat | StrictInt | None = None
    Sharpness: StrictFloat | StrictInt | None = None
