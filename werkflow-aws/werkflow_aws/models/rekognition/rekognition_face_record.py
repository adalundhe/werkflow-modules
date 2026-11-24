from __future__ import annotations
from pydantic import BaseModel
from .rekognition_face import RekognitionFace
from .rekognition_face_detail import RekognitionFaceDetail


class RekognitionFaceRecord(BaseModel):
    Face: RekognitionFace | None = None
    FaceDetail: RekognitionFaceDetail | None = None
