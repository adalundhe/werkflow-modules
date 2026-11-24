from __future__ import annotations
from pydantic import BaseModel, StrictInt


class RekognitionDetectLabelsImagePropertiesSettings(BaseModel):
    MaxDominantColors: StrictInt | None = None
