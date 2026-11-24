from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_bounding_box import RekognitionBoundingBox


class RekognitionComparedSourceImageFace(BaseModel):
    BoundingBox: RekognitionBoundingBox | None = None
    Confidence: StrictFloat | StrictInt | None = None
