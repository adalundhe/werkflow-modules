from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .rekognition_face_detail import RekognitionFaceDetail


class RekognitionFaceDetection(BaseModel):
    Timestamp: StrictInt | None = None
    Face: RekognitionFaceDetail | None = None
