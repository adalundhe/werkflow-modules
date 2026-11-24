from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_dominant_color import RekognitionDominantColor


class RekognitionInstance(BaseModel):
    BoundingBox: RekognitionBoundingBox | None = None
    Confidence: StrictFloat | StrictInt | None = None
    DominantColors: list[RekognitionDominantColor] | None = None
