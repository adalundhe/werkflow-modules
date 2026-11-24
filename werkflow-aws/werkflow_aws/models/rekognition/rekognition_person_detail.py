from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_face_detail import RekognitionFaceDetail


class RekognitionPersonDetail(BaseModel):
    Index: StrictInt | None = None
    BoundingBox: RekognitionBoundingBox | None = None
    Face: RekognitionFaceDetail | None = None
