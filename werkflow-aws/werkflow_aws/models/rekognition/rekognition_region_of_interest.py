from __future__ import annotations
from pydantic import BaseModel
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_point import RekognitionPoint


class RekognitionRegionOfInterest(BaseModel):
    BoundingBox: RekognitionBoundingBox | None = None
    Polygon: list[RekognitionPoint] | None = None
