from __future__ import annotations
from pydantic import BaseModel
from .rekognition_face_detail import RekognitionFaceDetail


class RekognitionSearchedFaceDetails(BaseModel):
    FaceDetail: RekognitionFaceDetail | None = None
